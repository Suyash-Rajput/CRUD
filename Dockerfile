FROM python:3.9

WORKDIR /app

COPY . /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV DATABASE_URL "mysql+pymysql://user:password@db:3306/mydatabase"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
