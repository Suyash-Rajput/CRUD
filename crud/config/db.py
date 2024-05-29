from sqlalchemy import create_engine, MetaData

class Connection:
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:123456@localhost:3306/product_info")
        self.conn = self.engine.connect()
        self.meta = MetaData()
