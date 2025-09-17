FROM python:3.11-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ app/
COPY eda.py model.py dashboard.py . 

RUN python eda.py \
 && python model.py \
 && python dashboard.py

FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=builder /app/dashboard.yaml ./dashboard.yaml
COPY --from=builder /app/data.csv ./data.csv
COPY --from=builder /app/model.pkl ./model.pkl
COPY --from=builder /app/app/app.py ./app/app.py

EXPOSE 9060
CMD ["python", "app/app.py"]
