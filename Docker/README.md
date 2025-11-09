# House Price Prediction API using FastAPI and Docker

## Overview

An end-to-end machine learning pipeline containerized with Docker. It trains a Linear Regression model on the California Housing dataset and serves predictions via a FastAPI REST API.

## Project Structure

```bash
├── src/
│   ├── ingest_data.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── evaluate.py
│   ├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Running the Docker File

```bash
# Build image
docker build -t house-price-fastapi .

# Run container
docker run -p 8000:8000 house-price-fastapi
```

The app will be available at http://localhost:8000/docs

## The proof of running docker container:

<img width="1244" height="424" alt="image" src="https://github.com/user-attachments/assets/e2fd8219-6abf-45dd-bc4f-0a43fc4477bf" />

## The sample of the app running on FastAPI:

<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/b4c9212c-8b3a-4361-88e6-b013481dbeb4" />

<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/745ccfd1-514d-405d-9418-618a9f4139ec" />


