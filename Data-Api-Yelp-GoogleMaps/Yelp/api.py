import requests
import json
import pandas as pd
from google.cloud import storage

# Define API Key, Search Type, and header
MY_API_KEY = 'FBiwlzgIGYRKWQMBbhOlVI7dmjv6mGKzcOLNERFe31wajHlxS1-NauL_dbzrpq040MWv_ExzqA4XNvbSO-Tcy2zYrA8XJn2khIzGk-BE5IFDodqPGstWcWJFOg11ZHYx'
BUSINESS_PATH = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % MY_API_KEY}

# List of locations you want to search
locations = ['Ca', "Fl", "Nv", "Ny", "Hi"]

# Create a client for Google Cloud Storage
storage_client = storage.Client()

for location in locations:
    PARAMETERS = {
        'term': '',
        'location': location,
        'categories': ''
    }

    # Make the API request
    response = requests.get(url=BUSINESS_PATH, params=PARAMETERS, headers=HEADERS)
    business_data = response.json()

    # Convert the data to a DataFrame
    df = pd.DataFrame(business_data['businesses'])

    # Save the DataFrame as a CSV file
    csv_filename = f'yelp_{location}.csv'
    df.to_csv(csv_filename, index=False)

    # Upload the CSV file to Google Cloud Storage bucket
    bucket_name = 'datasetsyelp'  # Replace with your bucket name
    folder_name = 'Yelp_API'  # Name of the folder within the bucket
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f'{folder_name}/{csv_filename}')
    blob.upload_from_filename(csv_filename)
