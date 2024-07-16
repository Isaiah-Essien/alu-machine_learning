from fastapi import FastAPI, HTTPException, status
import numpy as np
import joblib
from pydantic import BaseModel
import uvicorn


# Load the model
model = joblib.load('./ad_budgets_sales_model.joblib')

app = FastAPI()


class AdBudget(BaseModel):
    TV_ad_budget: float
    Radio_ad_budget: float
    Newspaper_ad_budget: float


@app.get('/', status_code=status.HTTP_200_OK)
async def home():
    return 'Isaiah Greets you, Marvin 😎'


@app.post('/predict', status_code=status.HTTP_200_OK)
async def predict(budget: AdBudget):
    try:
        features = np.array(
            [[budget.TV_ad_budget, budget.Radio_ad_budget, budget.Newspaper_ad_budget]])
        prediction = model.predict(features)
        return {'prediction': prediction[0]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Something went wrong: {e}")

if __name__ == "__main__":
    config = uvicorn.Config(app, host="127.0.0.1", port=8000)
    server = uvicorn.Server(config)
    server.run()
