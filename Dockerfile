FROM python:3.9

WORKDIR /app

COPY . /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DATABASE_URL "mysql+mysqldb://fastapi_user:fastapi_password@db:3306/fastapi_db"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
