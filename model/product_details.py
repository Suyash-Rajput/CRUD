from sqlalchemy import Table, Column, MetaData
from sqlalchemy.sql.sqltypes import Integer, String, Float
from crud.config.db import Connection

# Initialize the connection
mysql = Connection()


product_details = Table(
    'product_details', 
    mysql.meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('category', String(255)),
    Column('price', Float)
)

# Create the table in the database
mysql.meta.create_all(mysql.engine)
