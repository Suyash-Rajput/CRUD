# from sqlalchemy import create_engine, MetaData

# class Connection:
#     def __init__(self):
#         self.engine = create_engine("mysql+pymysql://root:123456@localhost:3306/product_info")
#         self.conn = self.engine.connect()
#         self.meta = MetaData()

from sqlalchemy import create_engine, MetaData

class Connection:
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:123456@localhost:3306/product_info")
        self.conn = self.engine.connect()
        self.meta = MetaData()

#     def check_connection(self):
#         try:
#             # Execute a query to retrieve the list of databases
#             result = self.conn.execute("SHOW DATABASES")
#             databases = result.fetchall()
#             print("Connection successful. Databases available:")
#             for db in databases:
#                 print(db[0])
#         except Exception as e:
#             print(f"Connection failed: {e}")

# # Example usage
# db_connection = Connection()
# db_connection.check_connection()

