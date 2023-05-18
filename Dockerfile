FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ app/

CMD ["uvicorn", "app:main", "--host", "0.0.0.0", "--port", "8000"]
