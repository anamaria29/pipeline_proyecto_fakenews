# Proyecto: Pipeline de Datos con IA - Fake News

## Descripción

Este proyecto consiste en el desarrollo de un pipeline completo de datos para la detección de noticias falsas mediante técnicas de inteligencia artificial.

El sistema permite procesar datos, almacenarlos en una base de datos, entrenar un modelo de machine learning y ofrecer predicciones a través de una aplicación interactiva.

---

## Problema

La propagación de noticias falsas representa un problema creciente en la era digital, afectando la toma de decisiones y la percepción pública.

---

## Objetivo

Desarrollar un pipeline de datos que permita clasificar noticias como falsas o reales utilizando aprendizaje automático.

---

## Arquitectura del Pipeline

El flujo del sistema es el siguiente:

CSV → ETL → PostgreSQL → Entrenamiento del modelo → Aplicación Streamlit → Predicción

---

## Base de Datos

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

---

## Dataset

Se utilizó el dataset **Fake and Real News Dataset** obtenido de Kaggle.

Contiene:
- Fake.csv
- True.csv

---

## ETL (Extracción, Transformación y Carga)

1. Lectura de archivos CSV  
2. Unión de datasets (fake y real)  
3. Creación de variable objetivo `label`  
4. Preparación del dataset final  
5. Carga a PostgreSQL  

---

## Modelo de Inteligencia Artificial

Se implementó un modelo de clasificación de texto basado en:

- Algoritmo: Logistic Regression  
- Vectorización: TF-IDF (Term Frequency - Inverse Document Frequency)  

### Variables:

- Entrada: texto de la noticia (`text`)  
- Salida: clasificación (0 = fake, 1 = real)  

---

## Métricas del Modelo

El modelo fue evaluado utilizando un conjunto de prueba:

- Accuracy: 0.98  
- Precision: 0.98  
- Recall: 0.98  
- F1-score: 0.98  

Esto indica un alto nivel de desempeño en la clasificación de noticias.

---

## Aplicación

Se desarrolló una aplicación interactiva utilizando **Streamlit**.

### Funcionalidades:

- Ingreso de texto por el usuario  
- Clasificación automática (Fake / Real)  
- Visualización de probabilidades  
- Nivel de confianza del modelo  
- Gráficos de distribución  

La aplicación permite demostrar el funcionamiento completo del pipeline.

---

## Tecnologías utilizadas

- Python  
- PostgreSQL  
- SQLAlchemy  
- Pandas  
- Scikit-learn  
- Streamlit  
- Joblib  
- GitHub  

---

## Archivos principales

- `load_data.py`: carga de datos a PostgreSQL  
- `train_model.py`: entrenamiento del modelo  
- `app.py`: aplicación web de predicción  

---

## Cómo ejecutar

1. Clonar repositorio:

git clone https://github.com/anamaria29/pipeline_proyecto_fakenews.git
cd pipeline_proyecto_fakenews

2. Crear entorno virtual.

python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias:

pip install -r requirements.txt

4. Entrenar modelo:

python3 train_model.py

4. Ejecutar aplicación:

streamlit run app.py


### Integrantes:
Guadalupe Casco, Adrián González y Ana María Ramírez
