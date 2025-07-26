FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

COPY round1B.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "round1B.py"]
