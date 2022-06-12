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
    logger : Logger object
        logger object for debuging


    Methods
    -------
    connect():
        Connects with database.
    update_products(rates):
        Update all products in database.
    get_products():
        Query all products from database.
    """
    def __init__(self, config: typing.Dict, logger):
        """
        Constructs all the necessary atributes for the SQLConnector object.

        Parrameters
        ----------
            config : dict
                database configuration
            logger : Logger object
                logger object for debuging
        """
        self.config = config
        self.logger = logger

    def connect(self):
        """
        Connects with database.

        Returns:
            conn: mysql connection object
        """
        try:
            conn = mysql.connector.connect(**self.config)
            self.logger.info("Got connection with database")
            self.logger.debug(conn)
            return conn
        except mysql.connector.Error as err:
            self.logger.error(f"{err}")
            raise SystemExit("Cannot connect with the database")

    def update_products(self, rates: typing.Dict[float, float]):
        """
        Update all products in database.

        Parrameters
        ----------
            rates: dict
                store currency rates
        """
        mydb = self.connect()
        
        try:
            cur = mydb.cursor()
            sql = """UPDATE Product
            SET UnitPriceUSD = UnitPrice * %s,
            UnitPriceEuro = UnitPrice * %s
            """
            if not isinstance(rates["usd"], float):
                raise ValueError("Invalid type passes as rates[\"usd\"]")
            if not isinstance(rates["euro"], float):
                raise ValueError("Invalid type passes as rates[\"euro\"]")
            cur.execute(sql, (rates["usd"], rates["euro"]))
            mydb.commit()
            mydb.close()
        except mysql.connector.Error as err:
            self.logger.error(f"{err}")
            raise SystemExit("Database error")
        except ValueError as err:
            self.logger.error(f"{err}")
            raise SystemExit("Invalid type passed as currency rate")
        self.logger.info("Products successfully updated")


    def get_products(self):
        """
        Query all products from database.

        Returns:
            results: list of products
        """
        mydb = self.connect()

        try:
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
            self.logger.info(f"Fetched {len(results)} products")
            self.logger.debug(results)
            return results
        except mysql.connector.Error as err:
            self.logger.error(f"{err}")
            raise SystemExit("Database error")
