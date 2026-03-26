from fastapi import FastAPI
from api import get_weather
from lstm_model import build_model, predict
from alerts import send_alert

app = FastAPI()

model = build_model()

@app.get("/")
def home():
    return {"message": "Crisis Monitoring API Running"}

@app.get("/predict")
def predict_risk():
    weather = get_weather()

    sequence = [[
        weather["temperature"],
        weather["humidity"],
        weather["pressure"]
    ]] * 10

    risk = predict(model, sequence)

    if risk == 2:
        send_alert()

    return {
        "weather": weather,
        "risk": risk
    }