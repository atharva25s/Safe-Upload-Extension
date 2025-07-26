from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from model_utils import load_models, preprocess_input

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models once at startup
rf_model, linear_model, training_columns = load_models()

# Define input schema
class FileMetadata(BaseModel):
    filename: str
    completefilepath: str
    fileextension: str
    filesize_str: str

@app.post("/predict")
def predict_confidentiality(data: FileMetadata):
    X, filesize_kb = preprocess_input(
        data.filename,
        data.completefilepath,
        data.fileextension,
        data.filesize_str,
        training_columns
    )

    rf_pred = rf_model.predict(X)[0]
    lin_pred = linear_model.predict(X)[0]

    return {
        "random_forest_prediction": rf_pred,
        "linear_regression_prediction": lin_pred,
        "raw_input_features": {
            "filename": data.filename,
            "completefilepath": data.completefilepath,
            "fileextension": data.fileextension,
            "filesize": data.filesize_str,
            "filesize_kb": filesize_kb
        }
    }