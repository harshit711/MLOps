FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["bash", "-c", "\
    echo 'Starting ML pipeline...' && \
    python src/ingest_data.py && \
    python src/train_model.py && \
    python src/evaluate.py && \
    echo 'Pipeline complete. Launching FastAPI server...' && \
    uvicorn src.app:app --host 0.0.0.0 --port 8000 \
"]