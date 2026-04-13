DROP TABLE IF EXISTS noticias_curadas;

CREATE TABLE noticias_curadas (
    id INTEGER,
    title TEXT,
    text TEXT,
    subject TEXT,
    date DATE,
    label INTEGER,
    title_length INTEGER,
    text_length INTEGER,
    word_count INTEGER
);
