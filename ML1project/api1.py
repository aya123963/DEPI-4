import pickle
from fastapi import FastAPI
import numpy as np


with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "House Price Prediction API"}

@app.post("/predict")
def predict(rooms: int, poverty: float, student_teacher_ratio: float):

    data = np.array([[rooms, poverty, student_teacher_ratio]])

    prediction = model.predict(data)

    return {
        "predicted_price": float(prediction[0])
    }