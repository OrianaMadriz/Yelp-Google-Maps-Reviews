# Yelp-Google-Maps-Reviews


<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/portada.PNG">
</p>

<!-- TABLA DE CONTENIDO -->
## Indice
<details open="open">
  <summary>Tabla de contenido: </summary>
  <ol>
    <li>
      <a href="#Datacket">Datacket</a>
      <ul>
        <li><a href="#Quienes-somos">¿Quienes somos?</a></li>
        <li><a href="#Nuestro-equipo">Nuestro equipo</a></li>
      </ul>
    </li>
    <li>
      <a href="#Planteamiento-del-problema">Planteamiento del problema</a>
    </li>
    <li>
      <a href="#Propuesta-de-proyecto">Propuesta de proyecto</a>
      <ul>
        <li><a href="#Objetivos">Objetivos</a></li>
        <li><a href="#Metodología-de-trabajo">Metodología de trabajo</a></li>
        <li><a href="#kpis">KPIs</a></li>
        <li><a href="#Alcance">Alcance</a></li>
        <li><a href="#Stack-tecnológico">Stack tecnológico</a></li>
        <li><a href="#Posibilidades-de-continuidad-del-proyecto">Posibilidades de continuidad del proyecto</a></li> 
        <li><a href="#Limitaciones">Limitaciones</a></li>
        <li><a href="#performance-del-modelo">Performance del modelo</a></li>
      </ul>
    </li>
    <li>
      <a href="#Cronología-general">Cronología general</a>
      <ul>
        <li><a href="#Diagrama-de-Gantt">Diagrama de Gantt</a></li>
      </ul>
    </li>     
  </ol>
</details>


## Datacket
### ¿Quienes somos?

Somos **Datacket** una consultora con amplia experiencia e innovación en diferentes sectores de la industria.

Nos enfocamos en brindar soluciones de análisis de datos, inteligencia de negocios y modelado predictivo de datos innovadores y personalizadas para nuestros clientes. Trabajamos estrechamente con ellos para identificar las habilidades y conocimientos clave que serán necesarios en el futuro. 

### Nuestro equipo
Nuestro equipo de expertos está constantemente actualizado en las últimas tendencias y tecnologías del mercado laboral para brindar soluciones prácticas y efectivas para nuestros clientes. En Datacket, estamos comprometidos con el éxito de nuestros clientes. 

+ [Ada Parhuana](https://github.com/Adapa22) -  Data Engineer
+ [Jesús Chávez](https://github.com/JChz6) - Data Analyst
+ [Jose Brito](https://github.com/abritoj) - Data Scientist
+ [Keily Lasso](https://github.com/valen-l) - Data Engineer
+ [Oriana Madriz](https://github.com/OrianaMadriz) - Data Scientist

## Planteamiento del problema

"Análisis y Sistema de recomendación de restaurantes basado en opiniones de los usuarios de Yelp y Google Maps en Estados Unidos"

La problemática se centra en la recopilación, procesamiento y análisis de datos de los estados con mayor atractivo turístico de los US para comprender la opinión de los usuarios, predecir tendencias de crecimiento o declive en el mercado de restaurantes, seleccionar ubicaciones estratégicas y desarrollar un sistema de recomendación personalizado para los usuarios.

Se seleccionaron los 5 estados con mayor flujo turístico anual de Estados Unidos:

1. California
2. Florida
3. Nueva York
4. Hawái
5. Nevada

 <p align="center">
  <img src="https://i.ibb.co/M1FFfGT/planteamiento.png">
</p>


## Propuesta de proyecto
Para lograr los objetivos planteados, se deberá realizar un análisis exhaustivo del mercado turístico y gastronómico en Estados Unidos, identificando lugares con alto potencial de atractivo y demanda. 

Realizar un estudio detallado de la competencia en el mercado turístico y gastronómico en los lugares seleccionados. Basado en el análisis del mercado y la competencia, se elaborarán directrices de marketing para los nuevos negocios turísticos y gastronómicos. Estas directrices incluirán estrategias de posicionamiento, segmentación de mercado, canales de promoción, branding y comunicación efectiva para atraer y fidelizar a los clientes. 

Se llevará a cabo un estudio exhaustivo de las tendencias actuales en la industria de restaurantes. Se identificarán las preferencias de los consumidores. Este análisis permitirá adaptar los conceptos y menús de los nuevos negocios a las tendencias emergentes.

Se realizará un análisis de los negocios más exitosos en cada zona seleccionada. Se examinarán aspectos como la calidad de los productos y servicios. Estos casos de éxito servirán como referencia para identificar las mejores prácticas y aplicarlas en los nuevos negocios.

Se implementará un sistema de recomendación basado en los gustos previos de los usuarios. Esto se logrará a través de la recopilación de datos sobre las preferencias gastronómicas y turísticas de los clientes, y el uso de algoritmos de recomendación inteligente. Este sistema permitirá ofrecer recomendaciones personalizadas a los usuarios, mejorando su experiencia y fomentando la fidelización.

### Objetivos

- Seleccionar los lugares de Estados Unidos mas atractivos para invertir en nuevos negocios turísticos y/o gastronómicos.
- Indagar a la competencia del mercado turístico y gastronómico.
- Proponer directrices para elaborar sus estrategias de marketing.
- Analizar las tendencias del rubro de restaurantes.
- Evaluar las características de los negocios mas exitosos en cada zona. 
- Desarrollar un sistema de recomendación basado en los gustos previos de los usuarios.

### Metodología de trabajo

Utilizamos Scrum como metodología de trabajo para trabajar de manera más eficiente y colaborativa, enfocados en la entrega de valor constante y adaptarnos a los cambios en los requisitos y objetivos del proyecto.

  <p align="center">
  <img src="https://i.ibb.co/dQZy25R/gantt.png">
</p>
 
### KPIs

1.  **Puntaje promedio por categoría:**
Mide la calidad percibida por los usuarios de las diferentes categorías por restaurante. Ej.: Comida rápida, comida vegetariana, comida coreana, comida marina. Se calcula segmentando los restaurantes por categorías y promediando el puntaje (de 1 a 5 estrellas) por cada categoría. Se puede calcular por ciudad o por localidad. Es útil para medir las preferencias y calidad del servicio que se ofrece en cada zona geográfica según el tipo del restaurante.

  *Objetivo:* Mantener el puntaje de la categoría en la que se va a invertir siempre entre 4 y 5 estrellas mensualmente.

2. **Cantidad de reseñas por restaurante:**
Con esto se busca medir la interacción en el restaurante (o restaurantes, si tiene varias sucursales). Suma el total de reseñas que se obtuvieron en plataformas sociales. Un aumento constante refleja el crecimiento de la relevancia y popularidad del negocio.

  *Objetivo:* Elevar la cantidad de reseñas por restaurante por lo menos un 15% anualmente.
  
3. **Puntaje promedio mensual de acuerdo a categorías:**
Se obtiene tres métricas de importancia para el cliente y por medio de minería de texto se extraen palabras clave de las reseñas, por ejemplo, al cliente le interesa saber la puntuación de los criterios. Es útil para estudiar a detalle el rendimiento de un negocio y encontrar puntos fuertes y oportunidad de mejora.

  + Atención (attention, service, fast, waitress, waiter, gentle, help, nice, person, etc.)

  + Valoración de la comida (beef, chicken, burger, delicious, superb, food, tasty, taste, flavour, meat, hamburger, yummy, etc.)

  + Valoración del local (Sight, place, street, seat, table, ambient, clean, dirty, filthy, beautiful, etc.)

Una vez segmentadas las reseñas de acuerdo a los objetivos, se promedia el puntaje de las mismas para calificar estos aspectos del restaurante.
  
  *Objetivo:* Mantener o aumentar el puntaje promedio mensual por encima de 4.5 en las categorías de atención, valoración de la comida y valoración del local.

4. **Impacto potencial promedio de los reviewers:**
Promedia el número de fans que tienen las personas que escribieron reseñas del negocio en Yelp. Es útil para establecer objetivos de marketing y el desarrollo de campañas de comunicación.

*Objetivo:* Mantener el Impacto Potencial Promedio de los Reviewers por encima de 100.

5. **Sentimiento por estado y tipo de restaurante:**
 Esto permite conocer la aceptación del público que tienen los diferentes tipos de restaurantes en cada estado. Esto puede resultar útil para segmentar de manera más precisa campañas de marketing o como un parámetro útil para decidir invertir en determinado tipo de restaurante en cada estado.
  
  *Objetivo:* Mantener el sentimiento positivo de la categoría del negocio o del estado a invertir por encima del 70% anualmente..

6. **Tasa mensual de satisfacción de los reviewers:**
Calcula el porcentaje de calificaciones positivas (4 o 5 estrellas) del total de puntuaciones que el restaurante recibió. Es útil para medir la reputación del negocio y establecer objetivos de mejora para el futuro.

  $$ (CantidadDeCalificaciones/CantidadDeCalificacionesPositivas)*100 $$
  
  *Objetivo:* Mantener la Tasa Mensual de Satisfacción de los Reviewers siempre por sobre el 85%.

### Modelo ER

<img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/DER.png">


<br>

### Alcance

El proyecto está dirigido al grupo inversor que busca identificar el rubro con el mayor margen de retorno de inversión dentro del sector turístico, de ocio y esparcimiento. El grupo inversor es el destinatario principal de las actividades y entregables del proyecto, ya que son ellos quienes desean tomar decisiones basadas en datos y bien analizadas estratégicamente para maximizar las ganancias de su inversión.

Además, el informe de recomendaciones generado como resultado del proyecto también puede ser de interés para otros actores involucrados en la industria turística, como consultores de inversión, profesionales de la industria, instituciones financieras y empresas relacionadas. Estos actores podrían utilizar el informe como referencia para comprender las oportunidades de inversión en el sector y tomar decisiones comerciales basadas en los hallazgos y recomendaciones presentados.

En general, el alcance del proyecto es ayudar al grupo inversor a identificar el rubro con mayor margen de retorno de inversión dentro del sector turístico, de ocio y esparcimiento. Para lograrlo, se llevarán a cabo actividades de análisis del sector, evaluación de subsectores clave, investigación de rubros prometedores, consulta a expertos en la industria, desarrollo de estrategias de inversión y presentación de un informe de recomendaciones. El objetivo final es proporcionar al grupo inversor la información necesaria para tomar decisiones informadas y estratégicas que maximicen el rendimiento de su inversión en el sector turístico.

+ Negocio objetivo: locales turisticos, locales de ocio y/o locales gastronómicos
+ Área geográfica: Estados Unidos
+ Periodo de información: 2010-2021
+ Fuente de información: Yelp, Google Maps.

### Stack tecnológico

+ Github: Alojamiento de nuestro repositorio.
+ Notion: Organización de tareas.
+ Visual Studio Code: Software para trabajar de forma local en el proyecto.
+ Google Colab: Servicio de Google para trabajar de forma colaborativa y en la nube.
+ Google Cloud Platform: Plataforma de computación en la nube que ofrece una amplia gama de servicios de infraestructura y aplicaciones en la nube.
+ Google Cloud Storage: Servicio Cloud de almacenamiento.
+ Google Cloud Function: Servicio sin servidor para ejecutar código en respuesta a eventos.
+ Google Cloud Scheduler: Servicio para programar tareas en la nube.
+ Google Big Query: Servicio para hacer análisis de datos de gran escala en la nube.
+ Google Cloud API's: Conjunto de API's que permite acceder a los servicios y datos en la nube.
+ Places API: API de Google que permite acceder a información detallada sobre lugares y establecimientos
+ Geocoding API: API de Google que permite convertir direcciones en coordenadas geográficas y viceversa.
+ Python: Lenguaje de programación usado para ciencia de datos.
+ Pandas: Libreria escrita para el lenguaje Python para la manipulación y el análisis de datos.
+ Matplotlib: Libreria en Python para crear visualizaciones de nuestros datos.
+ Seaborn: Libreria de visualización de datos de Python basada en matplotlib.
+ Scikit-learn: Libreria de aprendizaje automático de código abierto para el lenguaje de programación Python


### Posibilidades de continuidad del proyecto

Dado que el alcance actual del proyecto se centra en la identificación de rubros con mayor margen de retorno de inversión dentro del sector turístico, de ocio y esparcimiento, existen posibilidades de continuidad del proyecto para abordar aspectos adicionales que puedan estar fuera del alcance actual, como:

Investigación más profunda de subsectores específicos.
Análisis detallado de la competencia en rubros seleccionados.
Desarrollo de estrategias de marketing específicas para cada rubro.
Estudio de viabilidad financiera y análisis de riesgos más detallados.
Implementación y seguimiento de las estrategias de inversión propuestas.
Estas posibilidades de continuidad del proyecto pueden ser evaluadas y consideradas en futuras fases o etapas, una vez que se hayan completado los objetivos establecidos en el alcance actual.

### Limitaciones

Las posibles limitaciones del proyecto podrían incluir:

+ Disponibilidad de datos: La disponibilidad y accesibilidad de datos confiables y actualizados sobre el sector turístico, de ocio y esparcimiento podría ser limitada. Esto podría dificultar el análisis exhaustivo y preciso del mercado y la competencia.
+ Incertidumbre en el rendimiento de inversión: Aunque se realicen análisis y evaluaciones cuidadosas, no se puede garantizar con certeza el rendimiento de inversión en el rubro identificado como más prometedor. Factores externos, como cambios económicos, fluctuaciones del mercado y eventos imprevistos, pueden afectar los resultados esperados.
+ Complejidad de la competencia: La competencia en el sector turístico y de ocio puede ser intensa y diversa. Identificar y evaluar a todos los competidores relevantes puede ser un desafío, especialmente considerando la presencia de actores locales y regionales.
+ Aspectos legales y regulatorios: Las regulaciones gubernamentales y los requisitos legales relacionados con el sector turístico pueden variar según la ubicación geográfica y estar sujetos a cambios. Esto podría influir en las estrategias de inversión propuestas y requerir un seguimiento continuo de las actualizaciones regulatorias.
+ Factores externos impredecibles: El éxito de los negocios turísticos y de ocio también puede verse afectado por factores externos impredecibles, como desastres naturales, crisis económicas o pandemias. Estos eventos pueden impactar negativamente la demanda del mercado y generar incertidumbre en cuanto a la rentabilidad de la inversión.
+ Limitaciones de recursos y tiempo: Los recursos financieros, humanos y de tiempo asignados al proyecto pueden ser limitados. Esto puede influir en la cantidad de subsectores que se pueden evaluar en profundidad y en la extensión de los análisis realizados.
+ Barreras tecnológicas 
+ Todo área geográfica fuera de Estados Unidos

Es importante tener en cuenta estas limitaciones y manejarlas de manera adecuada durante la ejecución del proyecto. Se deben establecer estrategias de mitigación de riesgos y se debe tener flexibilidad para adaptarse a posibles cambios y desafíos que puedan surgir durante el proceso.

### Performance del modelo
Desarrollar un sistema de recomendación que recoge las reseñas hechas de un usuario, o de los usuarios a los que sigue, y sugiere otros negocios similares.

## Cronología general
### Diagrama de Gantt
Se emplea el uso del Diagrama de Gantt como herramienta que nos permite visualizar las actividades de progreso del proyecto y ajustar el plan según sea necesario.

<p align="center">
  <img src="https://github.com/Adapa22/PF-YelpGoogleMaps/blob/main/src/dgantt.PNG">
</p>



