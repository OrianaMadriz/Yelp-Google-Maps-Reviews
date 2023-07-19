import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def obtener_ciudades_con_mejor_review(estado):
    # Cargar el DataFrame con los datos de los negocios
    df = pd.read_csv('datamodelo5estadossinsentimiento.csv')  # Reemplaza 'ruta_del_archivo.csv' con la ruta real de tu archivo de datos
    
    # Filtrar el DataFrame por el estado seleccionado
    df_estado = df[df['state'].str.lower() == estado.lower()]
    
    # Inicializar el analizador de sentimientos
    sia = SentimentIntensityAnalyzer()
    
    # Calcular el puntaje de sentimiento para cada revisión
    df_estado['sentiment_score'] = df_estado['review'].apply(lambda x: sia.polarity_scores(x)['compound'])
    
    # Ordenar el DataFrame por puntaje de sentimiento descendente y seleccionar las 10 mejores ciudades
    df_top_ciudades = df_estado.sort_values(by='sentiment_score', ascending=False).head(10)
    
    # Obtener una lista de las ciudades y categorías con las mejores revisiones
    lista_ciudades_categorias = df_top_ciudades[['city', 'categories']].values.tolist()
    
    return lista_ciudades_categorias

# Ejemplo de uso
estado_seleccionado = 'NY'  # Reemplaza con el estado deseado en minúsculas ('NY', 'CA', 'HI', 'NV', 'FL')
lista_ciudades_categorias = obtener_ciudades_con_mejor_review(estado_seleccionado)

# Imprimir la lista de ciudades y categorías con las mejores revisiones
for ciudad, categorias in lista_ciudades_categorias:
    print("Ciudad:", ciudad)
    print("Categorías:", categorias)
    print("-----------------------")
