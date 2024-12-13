import streamlit as st
from function import (
    analyze_sentiment,
    translate_to_french,
    square_number,
    reverse_text,
    text_length,
)

st.title("Streamlit y FastAPI")

# Menu
option = st.sidebar.selectbox(
    "Seleccione una funcionalidad",
    ("Análisis de Sentimiento", "Traducción al Francés", "Cuadrado de un Numero", "Invertir Texto", "Longitud de un Texto")
)

# Funcionalidades
if option == "Análisis de Sentimiento":
    st.header("Análisis de Sentimiento")
    user_input = st.text_area("Escribe algo en ingles:")
    if st.button("Analizar sentimiento"):
        if user_input:
            result = analyze_sentiment(user_input)
            st.write(f"Texto: {result['text']}")
            st.write(f"Sentimiento: {result['sentiment']}")
        else:
            st.warning("Por favor ingrese un texto.")

elif option == "Traducción al Francés":
    st.header("Traducción al Francés")
    user_input = st.text_area("Escribe algo en ingles:")
    if st.button("Traducir"):
        if user_input:
            result = translate_to_french(user_input)
            st.write(f"Texto Original: {result['text']}")
            st.write(f"Traduccion: {result['translation']}")
        else:
            st.warning("Por favor ingrese un texto.")

elif option == "Cuadrado de un Numero":
    st.header("Cuadrado de un Numero")
    user_input = st.number_input("Escribe un numero:")
    if st.button("Calcular"):
        if user_input:
            result = square_number(user_input)
            st.write(f"Numero: {result['number']}")
            st.write(f"Cuadrado: {result['square']}")
        else:
            st.warning("Por favor ingrese un texto.")

elif option == "Invertir Texto":
    st.header("Invertir Texto")
    user_input = st.text_area("Escribe un texto:")
    if st.button("Invertir"):
        if user_input:
            result = reverse_text(user_input)
            st.write(f"Texto Original: {result['original']}")
            st.write(f"Texto Invertido: {result['reversed']}")
        else:
            st.warning("Por favor ingrese un texto.")

elif option == "Longitud de un Texto":
    st.header("Longitud de un Texto")
    user_input = st.text_area("Escribe un texto:")
    if st.button("Calcular"):
        if user_input:
            result = text_length(user_input)
            st.write(f"Texto: {result['text']}")
            st.write(f"Longitud: {result['length']}")
        else:
            st.warning("Por favor ingrese un texto.")