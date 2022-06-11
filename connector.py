import mysql.connector
import typing

class SQLConnector:
    def __init__(self, config: typing.Dict):
        self.config = config

    def _test_connection(self):
        with mysql.connector.connect(**self.config) as conn:
            print(conn)

    def connect(self):
        return mysql.connector.connect(**self.config)

    def update_products(self, rates: typing.Dict[float, float]):
        mydb = self.connect()
        cur = mydb.cursor()
        
        sql = """UPDATE Product
        SET UnitPriceUSD = UnitPrice * %s,
        UnitPriceEuro = UnitPrice * %s
        """

        cur.execute(sql, (rates['usd'], rates['euro']))
        mydb.commit()
        print(cur.rowcount, "records affected")
        mydb.close()

    def get_products(self):
        mydb = self.connect()
        cur = mydb.cursor()

        sql = """SELECT ProductID, DepartmentID, Category,
        IDSKU, ProductName, Quantity, UnitPrice, 
        UnitPriceUSD, UnitPriceEuro, Ranking,
        ProductDesc, UnitsInStock, UnitsInOrder
        FROM Product
        """

        cur.execute(sql)
        results = cur.fetchall()
        mydb.close()

        return results