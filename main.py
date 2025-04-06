from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import uvicorn

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model
model = joblib.load('beta_secretase_model.pkl')

@app.post("/predict")
async def predict(data: dict):
    try:
        descriptors = np.array(data["descriptors"]).reshape(1, -1)
        prediction = model.predict(descriptors)
        return {"pIC50": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

