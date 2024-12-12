from transformers import pipeline

# Cargar pipelines de Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")
translation_pipeline = pipeline("translation_en_to_fr")

def analyze_sentiment(text: str):
    """
    Analiza el sentimiento de un texto usando Hugging Face.
    """
    result = sentiment_pipeline(text)
    return {"text": text, "sentiment": result}

def translate_to_french(text: str):
    """
    Traduce texto del inglés al francés usando Hugging Face.
    """
    result = translation_pipeline(text)
    return {"text": text, "translation": result}

def square_number(number: int):
    """
    Calcula el cuadrado de un número.
    """
    return {"number": number, "square": number ** 2}

def reverse_text(text: str):
    """
    Invierte un texto.
    """
    return {"original": text, "reversed": text[::-1]}

def text_length(text: str):
    """
    Calcula la longitud de un texto.
    """
    return {"text": text, "length": len(text)}