
## API - Proceso de Extracción Automatizado

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/apir.PNG">
</p>

<!-- TABLA DE CONTENIDO -->
## Indice
<details open="open">
  <summary>Tabla de contenido: </summary>
  <ol>
    <li>
      <a href="#Proceso-de-Extracción-Automatizado">Proceso de Extracción Automatizado</a>
      <ul>
        <li><a href="#API">API</a></li>
        <li><a href="#Script">Script</a></li>
        <li><a href="#Cloud-Run">Cloud Run</a></li>
        <li><a href="#Cloud-Scheduler">Cloud Scheduler</a></li>
        <li><a href="#Data-Lake">Data Lake</a></li>
      </ul> 
    </li>
    <li>
      <a href="#Visión-General">Visión General</a>
    </li>
    <li>
      <a href="#Stack-Tecnológico">Stack Tecnológico</a>
    </li>
  </ol>
</details>

## API 
Las APIs de Yelp y Google Maps ofrecen a los dueños e inversionistas de restaurantes información valiosa a través de las reseñas de usuarios y otros datos relevantes. Estas reseñas ayudan a los dueños de restaurantes a mejorar la visibilidad e imagen de su negocio, tomar decisiones informadas basadas en las experiencias de los clientes, recibir retroalimentación para realizar mejoras continuas y realizar análisis competitivos para destacar en el mercado. En resumen, aprovechar las reseñas de usuarios y los datos proporcionados por estas plataformas beneficia a los dueños e inversionistas de restaurantes al impulsar la calidad del servicio, atraer a más clientes y lograr el éxito en el mercado gastronómico.

## Script
El código que hemos desarrollado tiene como objetivo ayudarnos a recopilar reseñas de restaurantes en diferentes ciudades y estados con mayor flujo turístico de los Estados Unidos. Utilizamos las APIs de Yelp y Google Places para obtener información sobre los restaurantes, como el nombre, la ubicación, las reseñas y otros detalles relevantes.

## Docker
Creamos una imagen de docker en la consola de GCP. Incluimos un archivo Dockerfile que describe los pasos necesarios para construir la imagen para luego subir la misma al registro de contenedores accesible desde GCP.

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/docker.gif">
</p>

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/docker2.gif">
</p>

## Container Registry
<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/cregistry.PNG">
</p>

## Cloud Run
Cloud Run es un servicio de GCP que nos permitió desplegar nuestra imagen de Docker  en un entorno sin servidor. Al utilizar Cloud Run, no necesitamos preocuparnos por la infraestructura subyacente, ya que el servicio se encarga de la administración de la misma. 

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/crun.PNG">
</p>

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/crun.gif">
</p>

## Cloud Scheduler
Cloud Scheduler es un servicio que nos permite programar la ejecución de tareas en la nube. Configuramos Cloud Scheduler para la ejecución de nuestro contenedor en Cloud Run  lo que nos ayuda a automatizar procesos y tareas recurrentes. La ejecución de nuestro contenedor se programó para ejecutarse automáticamente todos los lunes a las 9 AM.

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/cschh.PNG">
</p>

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/csch1.gif">
</p>

## Data Lake
Una vez que tenemos las reseñas, las organizamos y las almacenamos en un lugar seguro de nuestro un bucket en Google Cloud Storage. Este es un servicio en la nube proporcionado por Google que nos permite almacenar grandes volúmenes de datos en su formato original, sin estructuración previa. En nuestro Data Lake, los datos fueron almacenados luego del proceso de pipelines de extracción, proceso en el cual ya se los fitra y se guardan los datos limpios y listos para ser añadidos a Bigquery de forma automatizada.

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/cstorage.PNG">
</p>

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/cs11.gif">
</p>

## Visión General
La integración de la API de Yrlp y Google Maps nos permite recopilar y analizar reseñas de clientes en ciudades con mayor flujo de turismo de Estados Unidos. Esta información valiosa nos ayuda a comprender la experiencia y satisfacción de los usuarios, permitiéndonos tomar decisiones informadas para mejorar nuestro negocio como propietario e inversor en la industria de restaurantes. 

Mediante la automatización de los pipelines de extracción de datos hacia nuestro Data Lake, garantizamos la disponibilidad actualizada y confiable de los datos. Esta automatización ahorra tiempo y recursos al eliminar procesos manuales y nos brinda información actualizada para la toma de decisiones basadas en datos precisos

## Stack Tecnológico
+ Cloud Storage
+ Cloud Run
+ Container Registry
+ Cloud Scheduler
+ Python
+ Docker



