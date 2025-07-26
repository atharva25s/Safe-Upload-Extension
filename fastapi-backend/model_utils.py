import joblib
import pandas as pd

def load_models():
    rf_model = joblib.load("models/rf_model.pkl")
    linear_model = joblib.load("models/linear_model.pkl")
    training_columns = joblib.load("models/training_columns.pkl")
    return rf_model, linear_model, training_columns

def convert_filesize_to_kb(filesize_str):
    size = filesize_str.lower()
    if 'kb' in size:
        return float(size.replace('kb', '').strip())
    elif 'mb' in size:
        return float(size.replace('mb', '').strip()) * 1024
    elif 'gb' in size:
        return float(size.replace('gb', '').strip()) * 1024 * 1024
    return 0.0

def preprocess_input(filename, filepath, extension, filesize_str, training_columns):
    filesize_kb = convert_filesize_to_kb(filesize_str)
    data = pd.DataFrame([{
        'filename': filename,
        'completefilepath': filepath,
        'fileextension': extension,
        'filesize': filesize_kb
    }])

    encoded = pd.get_dummies(data)

    missing_cols = [col for col in training_columns if col not in encoded.columns]
    missing_df = pd.DataFrame(0, index=encoded.index, columns=missing_cols)

    encoded = pd.concat([encoded, missing_df], axis=1)
    encoded = encoded[training_columns]
    encoded = encoded[training_columns]

    return encoded, filesize_kb
