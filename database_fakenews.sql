-- Crear base de datos
CREATE DATABASE postgres;



-- Crear tabla principal
CREATE TABLE noticias (
    id SERIAL PRIMARY KEY,
    title TEXT,
    text TEXT,
    subject TEXT,
    date TEXT,
    label INTEGER
);