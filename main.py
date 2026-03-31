from fastapi import FastAPI
from textblob import TextBlob
from pydantic import BaseModel

app = FastAPI()

# Ορίζουμε τι δεδομένα θα δέχεται το API μας
class UserInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "AI Model is Live!", "instructions": "Go to /docs to test it."}

@app.post("/predict")
def predict_sentiment(input_data: UserInput):
    # Εδώ γίνεται η ανάλυση συναισθήματος
    analysis = TextBlob(input_data.text)
    
    # Το polarity είναι από -1 (πολύ αρνητικό) έως 1 (πολύ θετικό)
    score = analysis.sentiment.polarity
    
    if score > 0:
        sentiment = "Positive 😊"
    elif score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
        
    return {
        "text_received": input_data.text,
        "sentiment": sentiment,
        "confidence_score": score
    }