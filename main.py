import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Initialize FastAPI
app = FastAPI()

# Define the request body format for predictions
class PredictionFeatures(BaseModel):
    experience_level_encoded: float
    company_size_encoded: float
    employment_type_PT: int
    job_title_Data_Engineer: int
    job_title_Data_Manager: int
    job_title_Data_Scientist: int
    job_title_Machine_Learning_Engineer: int

# Load the model
model = joblib.load('lin_regress.sav')

# API Root endpoint
@app.get("/")
async def index():
    return {"message": "Welcome to the Data Science Income API. Use the /predict endpoint to get a salary prediction."}

# Prediction endpoint
@app.post("/predict")
async def predict(features: PredictionFeatures):

    # Create input DataFrame for prediction
    input_data = pd.DataFrame([{
        "experience_level_encoded": features.experience_level_encoded,
        "company_size_encoded": features.company_size_encoded,
        "employment_type_PT": features.employment_type_PT,
        "job_title_Data_Engineer": features.job_title_Data_Engineer,
        "job_title_Data_Manager": features.job_title_Data_Manager,
        "job_title_Data_Scientist": features.job_title_Data_Scientist,
        "job_title_Machine_Learning_Engineer": features.job_title_Machine_Learning_Engineer
    }])

    # Get the columns the model was trained with
    model_columns = model.feature_names_in_

    # Add missing columns with default value = 0
    for col in model_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    # Reorder columns to match model training
    input_data = input_data[model_columns]

    # Predict using the loaded model
    prediction = model.predict(input_data)[0]

    return {
        "predicted_salary": float(prediction)
    }

# Run with python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)