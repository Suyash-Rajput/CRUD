import json
import uvicorn
from  crud.tables.model import product_details
from crud.tables.schema import user 
from crud.config.db import Connection
from fastapi import FastAPI

mysql =  Connection()
app = FastAPI()


@app.post("/create/")
async def create_id(query : user):
    mysql.conn.execute(product_details.insert().values(
        id = query.id,
        name = query.name,
        category = query.category,
        price = query.price
    ))
    return f"Successfully inserted data at {query.id} id"


@app.get("/read")
async def read_id():
    mysql.conn.execute(product_details.select()).fetchall()


@app.put("/update/{id}")
async def update_id(id: int, query: user):
    mysql.conn.execute(product_details.update().values(
        id = query.id,
        name = query.name,
        category = query.category,
        price = query.price
    ).where(product_details.c.id == id))
    return f"Successfully updated data at {query.id} id"


@app.delete("/delete/{id}")
async def delete_id(id: int):
    mysql.conn.execute(product_details.delete().where(product_details.c.id == id)).fetchall()
    return f"Successfully deleted data at {id} id"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)