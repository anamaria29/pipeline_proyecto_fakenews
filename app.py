import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main {
        background-color: #071122;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, h4, p, label, div {
        color: white;
    }

    .custom-card {
        background: linear-gradient(135deg, #0f172a, #081226);
        padding: 24px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        margin-bottom: 18px;
    }

    .result-fake {
        background: linear-gradient(135deg, #7f1d1d, #991b1b);
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        font-size: 30px;
        font-weight: 700;
        color: white;
        box-shadow: 0 10px 28px rgba(127,29,29,0.35);
        margin-bottom: 12px;
    }

    .result-real {
        background: linear-gradient(135deg, #14532d, #166534);
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        font-size: 30px;
        font-weight: 700;
        color: white;
        box-shadow: 0 10px 28px rgba(22,101,52,0.35);
        margin-bottom: 12px;
    }

    .muted {
        color: #cbd5e1 !important;
        font-size: 15px;
    }

    div[data-testid="stTextArea"] textarea {
        background-color: #0f172a !important;
        color: white !important;
        border-radius: 16px !important;
        border: 1px solid #334155 !important;
        min-height: 240px !important;
        font-size: 16px !important;
    }

    div[data-testid="stButton"] button {
        background: linear-gradient(90deg, #06b6d4, #3b82f6);
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 14px;
        padding: 0.8rem 1.2rem;
        width: 100%;
    }

    div[data-testid="stButton"] button:hover {
        filter: brightness(1.08);
        transition: 0.2s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

if "texto" not in st.session_state:
    st.session_state.texto = ""

fake_example = """
Breaking: NASA confirms aliens landed yesterday and secret agents are hiding the truth from the public.
"""

real_example = """
The United Nations held a climate meeting this week to discuss emissions targets and energy transition strategies among member countries.
"""

with st.sidebar:
    st.markdown("## Panel del modelo")
    st.markdown("**Modelo:** Logistic Regression")
    st.markdown("**Vectorización:** TF-IDF")
    st.markdown("**Objetivo:** Clasificar noticias como Fake o Real")
    st.markdown("---")
    st.markdown("### Dataset")
    st.markdown("- `Fake.csv`")
    st.markdown("- `True.csv`")
    st.markdown("---")
    st.markdown("### Cómo usar")
    st.markdown("""
1. Escribe o pega una noticia  
2. Presiona **Analizar noticia**  
3. Observa clasificación, probabilidades y confianza
""")

st.markdown("""
<div class="custom-card">
    <h1 style="font-size:52px; margin-bottom:8px;">Fake News Detector</h1>
    <p class="muted" style="font-size:18px;">
        Aplicación de inteligencia artificial para clasificar noticias como falsas o reales
    </p>
</div>
""", unsafe_allow_html=True)

top1, top2 = st.columns([2.2, 1])

with top1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Texto de la noticia")
    texto = st.text_area(
        "",
        value=st.session_state.texto,
        placeholder="Pega aquí el contenido de una noticia para analizarla..."
    )
    st.session_state.texto = texto

    b1, b2, b3 = st.columns(3)
    with b1:
        analizar = st.button("Analizar noticia")
    with b2:
        if st.button("Ejemplo fake"):
            st.session_state.texto = fake_example.strip()
            st.rerun()
    with b3:
        if st.button("Ejemplo real"):
            st.session_state.texto = real_example.strip()
            st.rerun()

    if st.button("Limpiar texto"):
        st.session_state.texto = ""
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

with top2:
    st.markdown("""
    <div class="custom-card">
        <h3>Resumen</h3>
        <p class="muted">
            Esta app consume un modelo de machine learning entrenado con noticias etiquetadas
            y devuelve una clasificación con nivel de confianza.
        </p>
        <p class="muted">
            Ideal para demostrar el componente final del pipeline de datos con IA.
        </p>
    </div>
    """, unsafe_allow_html=True)

if "analizar" not in st.session_state:
    st.session_state.analizar = False

if analizar:
    st.session_state.analizar = True

if st.session_state.analizar and st.session_state.texto.strip():
    texto = st.session_state.texto.strip()
    texto_vec = vectorizer.transform([texto])
    pred = model.predict(texto_vec)[0]
    probs = model.predict_proba(texto_vec)[0]

    fake_prob = float(probs[0])
    real_prob = float(probs[1])
    confianza = max(fake_prob, real_prob)

    st.markdown("## Resultado del análisis")

    if pred == 0:
        st.markdown(
            f'<div class="result-fake">⚠️ Clasificación: FAKE NEWS<br><span style="font-size:18px;">Confianza del modelo: {confianza:.2%}</span></div>',
            unsafe_allow_html=True
        )
        interpretacion = "El modelo detecta patrones más cercanos a una noticia falsa."
    else:
        st.markdown(
            f'<div class="result-real">✅ Clasificación: REAL NEWS<br><span style="font-size:18px;">Confianza del modelo: {confianza:.2%}</span></div>',
            unsafe_allow_html=True
        )
        interpretacion = "El modelo detecta patrones más cercanos a una noticia real."

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Probabilidad Fake", f"{fake_prob:.2%}")
    m2.metric("Probabilidad Real", f"{real_prob:.2%}")
    m3.metric("Palabras", f"{len(texto.split())}")
    m4.metric("Caracteres", f"{len(texto)}")

    st.subheader("Confianza del modelo")
    st.progress(int(confianza * 100))

    c1, c2 = st.columns([1.2, 1])

    with c1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.subheader("Distribución de probabilidad")
        chart_df = pd.DataFrame({
            "Clase": ["Fake", "Real"],
            "Probabilidad": [fake_prob, real_prob]
        }).set_index("Clase")
        st.bar_chart(chart_df)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.subheader("Interpretación")
        st.write(interpretacion)
        st.write(f"Nivel de confianza estimado: **{confianza:.2%}**")
        st.write("La predicción se basa en patrones lingüísticos aprendidos durante el entrenamiento del modelo.")
        st.markdown('</div>', unsafe_allow_html=True)