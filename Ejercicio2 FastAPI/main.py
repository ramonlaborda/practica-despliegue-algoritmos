from fastapi import FastAPI
from function import (analyze_sentiment, translate_to_french, square_number, reverse_text, text_length)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API modularizada con FastAPI y Hugging Face"}

@app.get("/sentiment/{text}")
def get_sentiment(text: str):
    return analyze_sentiment(text)

@app.get("/translate/{text}")
def get_translation(text: str):
    return translate_to_french(text)

@app.get("/square/{number}")
def get_square(number: int):
    return square_number(number)

@app.get("/reverse/{text}")
def get_reversed(text: str):
    return reverse_text(text)

@app.get("/length/{text}")
def get_length(text: str):
    return text_length(text)