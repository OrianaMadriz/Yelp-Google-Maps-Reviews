import requests
import pandas as pd
from datetime import datetime
from google.cloud import storage

API_KEY = "API KEY HERE"

states = ["California", "Florida", "New York", "Nevada", "Hawaii"]

data_list = []

# Función lambda para asignar valores de sentimiento
def assign_sentiment(rating):
    if rating == 3.0:
        return "neutral"
    elif rating > 3.0:
        return "positivo"
    else:
        return "negativo"

for state in states:
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+{state}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "OK":
        results = data["results"]
        for result in results:
            place_id = result["place_id"]
            detail_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}"
            detail_response = requests.get(detail_url)
            detail_data = detail_response.json()

            if detail_data["status"] == "OK":
                detail_result = detail_data["result"]
                user_reviews = detail_result.get("reviews", [])
                for review in user_reviews:
                    user_name = review.get("author_name", "")
                    rating = review.get("rating", "")
                    review_text = review.get("text", "")
                    time = review.get("time", "")
                    date = datetime.fromtimestamp(int(time)).strftime("%Y-%m-%d %H:%M:%S")
                    restaurant_name = detail_result.get("name", "")
                    restaurant_location = detail_result.get("formatted_address", "")
                    gmap_id = detail_result.get("place_id", "")
                    category = detail_result.get("types", "")
                    price_level = detail_result.get("price_level", "")
                    user_ratings_total = detail_result.get("user_ratings_total", "")
                    latitude = detail_result.get("geometry", {}).get("location", {}).get("lat", "")
                    longitude = detail_result.get("geometry", {}).get("location", {}).get("lng", "")

                    sentiment = assign_sentiment(rating)

                    data_list.append({"user_name": user_name, "rating": rating, "reviews": review_text,
                                      "date": date, "restaurant_name": restaurant_name,
                                      "restaurant_location": restaurant_location, "gmap_id": gmap_id,
                                      "category": category, "price_level": price_level,
                                      "user_ratings_total": user_ratings_total, "latitude": latitude,
                                      "longitude": longitude, "state": state, "sentiment": sentiment})

# Convertir la lista de diccionarios en un DataFrame
df = pd.DataFrame(data_list)

# Escribir el DataFrame como un archivo CSV en Cloud Storage
client = storage.Client()
bucket = client.bucket("datos-apis")
blob = bucket.blob("places_api.csv")
blob.upload_from_string(df.to_csv(index=False), "text/csv")
