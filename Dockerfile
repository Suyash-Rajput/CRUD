FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
ENV DATABASE_URL="mysql+mysqldb://fastapi_user:fastapi_password@10000/fastapi_db"

EXPOSE 8000

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
