FROM python:3.11-slim

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-por

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0.8080"]