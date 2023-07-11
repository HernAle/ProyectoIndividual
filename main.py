from fastapi import FastAPI
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title='Proyeco Indiviual - MLOps | Cristaldo Hernan',
              description='API de funciones y recomendacion')

#Carga de datasets
df_movies = pd.read_csv('movies_etl.csv')
df_eda = pd.read_csv('movies_eda.csv') 

#Funcion ingreso de idioma y retorno la cantidad de peliculas
@app.get('/peliculas_idioma/({idioma})')
def peliculas_idioma(idioma):
    idioma = idioma.lower()
    if idioma in df_movies['original_language'].values:
        df_peliculas_filtradas = df_movies[df_movies['original_language'] == idioma]
        cantidad_peliculas = len(df_peliculas_filtradas)
        return {'idioma': idioma, 'cantidad':cantidad_peliculas}
    else:
        return 'valor invalido'

#Funcion ingreso de titulo y retorno de duracion y anio de la misma
@app.get('/peliculas_duracion/({titulo})')
def peliculas_duracion(titulo):
    titulo = titulo.lower()
    if titulo in df_movies['title'].values:
        df_pelicula = df_movies[df_movies['title'] == titulo]
        runtime = df_pelicula['runtime'].values.item()
        year = df_pelicula['year'].values.item()
        return {'titulo': titulo, 'duracion': runtime, 'anio': year}
    else:
        return 'valor invalido'
    

#Funcion ingreso de franquicia y retorno de ganancia total y promedio
@app.get('/franquicia/({franquicia})')
def franquicia(franquicia):
    franquicia = franquicia.lower()
    ganancia_total = 0
    if franquicia in df_movies['collection'].values:
        df_franquicia = df_movies[df_movies['collection'] == franquicia]
        ganancias = df_franquicia['revenue'].values[:]
        for ganancia in ganancias:
            ganancia_total += ganancia
        return {'franquicia': franquicia,'ganancia total':ganancia_total,'ganancia promedio': ganancia_total / len(ganancias)}
    else:
        return 'valor invalido'
    

#Funcion ingreso de pais y retorno de cantidad de peliculas por pais
@app.get('/peliculas_pais/({pais})')
def peliculas_pais(pais):
    pais = pais.lower()
    if pais in df_movies['country'].values:
        df_pais = df_movies[df_movies['country'] == pais]
        return {'pais': pais,'cantidad de peliculas':len(df_pais)}
    else:
        return 'valor invalido'
    
#Funcion ingreso de productora y retorno de cantidad de peliculas y ganancia total de la productora
@app.get('/productoras_exitosas/({productora})')
def productoras_exitosas(productora):
    productora = productora.lower()
    ganancia_total = 0
    df_movies['companies'] = df_movies['companies'].fillna('')
    df_productoras = df_movies[df_movies['companies'].str.contains(productora)]
    if len(df_productoras) != 0:
        ganancias = df_productoras['revenue'].values[:]
        for ganancia in ganancias:
            ganancia_total += ganancia
        return {'productora': productora, 'cantidad de peliculas': len(df_productoras), 'ganancia total': ganancia_total}
    else:
        return 'valor invalido'

    

#Funcion para agregar un prefijo a cada array 
def agregar_prefijo(array, prefijo):
    array_nuevo = []
    for elemento in array:
        nuevo_elemento = f'{prefijo}:{elemento}'
        array_nuevo.append(nuevo_elemento)
    return np.array(array_nuevo)

# Funcion ingreso de director y retorno de titulo, fecha, retorno de inversion, costo y ganancia de cada pelicula
@app.get('/get_director/({director})')
def get_director(director):
    director = director.lower()
    df_peliculas = df_movies[df_movies['director'] == director]
    lista = []  # Inicializar lista como una lista vacía
    if len(df_peliculas) != 0:
        titulo = df_peliculas['title'].values[:]
        titulo = agregar_prefijo(titulo, 'titulo')
        fecha = pd.to_datetime(df_peliculas['release_date'], errors='coerce')
        fecha = np.datetime_as_string(fecha, unit='D')
        fecha = agregar_prefijo(fecha, 'fecha de lanzamiento')
        retorno = df_peliculas['return'].values[:]
        retorno = agregar_prefijo(retorno, 'retorno')
        costo = df_peliculas['budget'].values[:]
        costo = agregar_prefijo(costo, 'costo:')
        ganancia = df_peliculas['revenue'].values[:]
        ganancia = agregar_prefijo(ganancia, 'ganancia')

        lista = list(zip(titulo, fecha, retorno, costo, ganancia))
    return f'director:{director}', lista

