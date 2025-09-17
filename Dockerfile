FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY preprocessed.csv logreg_model.pkl dashboard.yaml explainer.joblib ./


EXPOSE 9060
CMD ["python", "app/app.py"]
