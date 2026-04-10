# Proyecto: Pipeline de Datos con IA - Fake News

## Descripción

Este proyecto consiste en el desarrollo de un pipeline completo de datos para la detección de noticias falsas mediante técnicas de inteligencia artificial.

El sistema permite procesar datos, almacenarlos en una base de datos, entrenar un modelo y ofrecer predicciones a través de una aplicación.



## Problema

La propagación de noticias falsas representa un problema creciente en la era digital, afectando la toma de decisiones y la percepción pública.



## Objetivo

Desarrollar un pipeline de datos que permita clasificar noticias como falsas o reales utilizando aprendizaje automático.



##  Base de Datos

Se utilizó PostgreSQL para el almacenamiento de datos.

### Base de datos:
- postgres

### Tabla principal:
- noticias

### Estructura:

| Columna | Descripción |
|--------|------------|
| id | Identificador único |
| title | Título |
| text | Contenido |
| subject | Categoría |
| date | Fecha |
| label | 0 = fake, 1 = real |



## Dataset

Se utilizó el dataset "Fake and Real News Dataset" obtenido de Kaggle.

Contiene:
- Fake.csv
- True.csv



## Tecnologías utilizadas

- Python
- PostgreSQL
- SQLAlchemy
- Pandas
- GitHub



## Pipeline

1. Extracción de datos desde CSV
2. Transformación (limpieza y etiquetado)
3. Carga a base de datos PostgreSQL
4. Entrenamiento de modelo de IA
5. Predicción mediante aplicación


## Cómo ejecutar

1. Clonar repositorio:

git clone https://github.com/anamaria29/pipeline_proyecto_fakenews.git

2. Crear entorno virtual.
3. Instalar dependencias (pandas y sqlalchemy).
4. Ejecutar carga de datos.

### Integrantes:
Guadalupe Casco, Adrián González y Ana María Ramírez
