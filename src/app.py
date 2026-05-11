from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI(title="NvN Prime Churn Predictor")

model = joblib.load('models/churn_model.pkl')

class CustomerData(BaseModel):
    session_duration: float
    pages_visited: int
    previous_purchase: int
    discount_applied: int
    device_type_desktop: int
    device_type_mobile: int
    device_type_tablet: int

@app.post('/predict')
def predict(data: CustomerData):
    # Convert input to DF for XGBoost
    df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(df)

    return {'churn_prediction': int(prediction[0])}
