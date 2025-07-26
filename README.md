# Safe-Upload-Extension

## Overview

**Safe-Upload-Extension** is a browser extension designed to enhance the security of web applications by detecting and warning users about potentially sensitive or confidential files during upload. It uses trained machine learning models to assess the risk level of a file in real time, helping prevent accidental data exposure or leaks.


## What does it do?

-  **Scans files before upload** on any website
-  **Predicts file confidentiality** using ML models (Linear & Random Forest)
-  **Warns users** if a file is classified as sensitive or confidential
-  Uses metadata and content-based features (filename, size, extension, entropy, etc.)
-  Works as a browser extension that integrates seamlessly with upload forms
-  Sends file features to a local FastAPI backend for prediction


## How does it work?

1.  **ML Models (Random Forest & Linear)**  
   - Trained on labeled file datasets to predict a "confidentiality score".

2.  **FastAPI Backend**  
   - Exposes a `/predict` API that accepts file features and returns predictions.
   - Runs locally or can be deployed to AWS using ECS & Docker.

3.  **Browser Extension**  
   - Injects a content script into websites
   - Detects file inputs and intercepts selected files
   - Extracts and merges metadata features from the file
   - Sends features to the backend
   - Displays a warning popup if a file is deemed sensitive

4.  **CI/CD Pipeline**  
   - GitLab CI automatically builds Docker image, pushes to Docker Hub, and deploys it to AWS ECS.

## How does it look?
    (Architecture)[favicon_io/arch.png]

## Tech Stack

| Layer             | Technology                       |
|-------------------|----------------------------------|
|  Extension        | JavaScript, Manifest V3          |
|  Backend API      | FastAPI (Python 3.10)            |
|  ML Models        | Scikit-learn (Linear, RandomForest) |
|  Containerization | Docker                           |
|  Deployment       | AWS ECS (Fargate or EC2)         |
|  CI/CD            | GitLab CI/CD + DockerHub         |
|  File Features    | File name, extension, size, entropy, string patterns, etc. |



## Local Setup

1. Clone the repository
```bash
    git clone https://gitlab.com/atharva25s/safe-upload-backend.git
```
- You will requiring only Extensions Directory

2. On your browser search for
```bash
    chrome://extensions
```

3. Enable Developer Mode and `Load Unpacked` the entire Extensions Folder


3. Pull the backend image from Docker
```bash
    docker run -d --name backend -p 8000:8000 atharva25s/safe-upload-backend:latest
```

- Backend will be available at
`http://localhost:8000/predict`




