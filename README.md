<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# DATA SCIENCE - PROYECTO INDIVIDUAL Nº1 

## Machine Learning Operations (MLOps)

<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>

### Contexto
---
En este proyecto como MLOps Engineer, nos enfrentamos al desafío de desarrollar un sistema de recomendación de peliculas.<br>
Sin embargo, encontramos que los datos disponibles son de baja calidad y carecen de estructura, de modo que nuestro objetivo es transformar estos datos, establecer procesos automatizados y construir un modelo mínimo viable (MVP).<br>
A través de la combinación de habilidades en ciencia de datos, nos enfrentamos al desafío de brindar recomendaciones personalizadas y mejorar la experiencia de los usuarios.

### Data Engineering
---
Para el proyecto se procedio a efectuar una serie de **`TRANSFORMACIONES`** solicitadas sobre un dataset dado:

- Algunos campos, como **`belongs_to_collection`**, **`production_companies`** y otros (ver diccionario de datos) están anidados, debimos desanidarlos para poder hacer alguna de las consultas de la API.
- Los valores nulos de los campos **`revenue`**, **`budget`** deben ser rellenados por el número **`0`**.
- Los valores nulos del campo **`release date`** deben eliminarse.
- De haber fechas, deberán tener el formato **`AAAA-mm-dd`**, además deberán crear la columna **`release_year`** donde extraerán el año de la fecha de estreno.
- Crear la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hay datos disponibles para calcularlo, deberá tomar el valor **`0`**.
- Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`poster_path`** y **`homepage`**.

### API
---
Se debio disponibilizar los siguientes endpoints usando el framework **`FastAPI`**:

- def **peliculas_idioma( *`Idioma`: str* )**:
Se ingresa un idioma y debe devolver la cantidad de películas producidas en ese idioma.

Ejemplo de retorno: *`X` cantidad de películas fueron estrenadas en `idioma`*
         
- def **peliculas_duracion( *`Pelicula`: str* )**:
Se ingresa una pelicula y debe devolver la la duracion y el año.

Ejemplo de retorno: *`X` . Duración: `x`. Año: `xx`*

- def **franquicia( *`Franquicia`: str* )**:
Se ingresa la franquicia y debe devolver la cantidad de peliculas, ganancia total y promedio

Ejemplo de retorno: *La franquicia `X` posee `X` peliculas, una ganancia total de `x` y una ganancia promedio de `xx`*

- def **peliculas_pais( *`Pais`: str* )**:
Se ingresa un país y debe devolver la cantidad de peliculas producidas en el mismo.

Ejemplo de retorno: *Se produjeron `X` películas en el país `X`*

- def **productoras_exitosas( *`Productora`: str* )**:
Se ingresa la productora y debe devolver el revenue total y la cantidad de peliculas que realizo. 

Ejemplo de retorno: *La productora `X` ha tenido un revenue de `x`*

- def **get_director( *`nombre_director`* )**:
Se ingresa el nombre de un director y debe devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.


### Análisis exploratorio de los datos: _(Exploratory Data Analysis-EDA)_
---
Con el fin de comprender mejor los datos transformados, se han llevado acabo un EDA sobre los valores del conjunto de datos.<br>
Este analisi tenia como objetivo encontrar relaciones entre los datos y comprender su importancia.<br>
Algunas de la tecnicas utilizadas incluyeron examinar estadisticamente las variables numericas, identificar variables categoricas, explorar correlaciones entre variables y analisis basados en los campos.

### Sistema de recomendación
--- 
Para lograr realizar el modelo de Machine Learning se utilizo como criterios filtrar el dataset para las peliculas con mayor impacto del publico, de modo que se hizo uso de los campos de votos (mejor puntaje y mayor cantidad de votos)<br>
Creando una muestra que no tenga problemas de ejecucion por tamaño ni recursos.

Tambien se trabajo en el armado de vectores numericos para poder aplicar el modelo de similitud de coseno.<br>
Este trabajo no fue sencillo ya que se debio crear primeramente un vector de tipo string con los campos mas relevantes para realizar un sistema de recomendacion.

- def **recomendacion( *`titulo`* )**:
Se ingresa el nombre de una película y debe devolver una lista de 5 peliculas similares como recomendacion.

### Deployment
---
Para el deploy de la API, se hará uso de **`FASTAPI`** junto a la plataforma **`Render`**.<br>
Se encuentrar en ejecucion en el siguiente link: https://proyect-service3.onrender.com/docs

### Video
---
Para poder observar pasos del proceso y una explicación mas detallada acerca de los trabajado en el dataset, accede al siguiente link:<br>
https://www.youtube.com/watch?v=gCmzBzwLm64

