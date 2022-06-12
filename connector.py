import mysql.connector
import typing


class SQLConnector:
    """
    A class to represent a SQL connector.

    ...

    Attributes
    ----------
    config : dict
        database configuration


    Methods
    -------
    connect():
        Connects with database.
    update_products(rates):
        Update all products in database.
    get_products():
        Query all products from database.
    """
    def __init__(self, config: typing.Dict):
        """
        Constructs all the necessary atributes for the SQLConnector object.

        Parrameters
        ----------
            config : dict
                database configuration
        """
        self.config = config

    def _test_connection(self):
        with mysql.connector.connect(**self.config) as conn:
            print(conn)

    def connect(self):
        """
        Connects with database.

        Returns:
            conn: mysql connection object
        """
        return mysql.connector.connect(**self.config)

    def update_products(self, rates: typing.Dict[float, float]):
        """
        Update all products in database.

        Parrameters
        ----------
            rates: dict
                store currency rates
        """
        mydb = self.connect()
        cur = mydb.cursor()

        sql = """UPDATE Product
        SET UnitPriceUSD = UnitPrice * %s,
        UnitPriceEuro = UnitPrice * %s
        """

        cur.execute(sql, (rates["usd"], rates["euro"]))
        mydb.commit()
        print(cur.rowcount, "records affected")
        mydb.close()

    def get_products(self):
        """
        Query all products from database.

        Returns:
            results: list of products
        """
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
