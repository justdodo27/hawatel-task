import argparse
import logging
import datetime as dt
from currency import CurrencyFetch
from connector import SQLConnector
from export import Exporter

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for products extraction')
    parser.add_argument("--host", type=str, default='127.0.0.1')
    parser.add_argument("--user", type=str, default='user')
    parser.add_argument("--password", type=str, default='user')
    parser.add_argument("--db", type=str, default='mydb')
    parser.add_argument("--export", type=bool, default=False)
    parser.add_argument("--type", type=str, default='excel')
    parser.add_argument("--filename", type=str, default='./export')
    parser.add_argument("--log_path", type=str, default='./')

    args = parser.parse_args()
    
    date = dt.datetime.now()
    logging.basicConfig(filename=f"{args.log_path}log-{date.strftime('%d-%m-%Y %H:%M:%S')}.txt", filemode='w', format="%(levelname)s:%(message)s", level=logging.DEBUG)
    logger = logging.getLogger('script logger')

    CONFIG = {
        "host": args.host,
        "user": args.user,
        "password": args.password,
        "database": args.db,
    }

    fetchUSD = CurrencyFetch(code="usd", logger=logger)
    fetchEuro = CurrencyFetch(code="eur", logger=logger)
    usd_rate = fetchUSD._fetch()
    euro_rate = fetchEuro._fetch()
    rates = {"usd": usd_rate["rates"][0]["mid"], "euro": euro_rate["rates"][0]["mid"]}

    connector = SQLConnector(config=CONFIG, logger=logger)
    connector.update_products(rates=rates)

    if args.export == True:
        products = connector.get_products()
        exporter = Exporter(
            data=products,
            columns_names=[
                "ProductID",
                "DepartmentID",
                "Category",
                "IDSKU",
                "ProductName",
                "Quantity",
                "UnitPrice",
                "UnitPriceUSD",
                "UnitPriceEuro",
                "Ranking",
                "ProductDesc",
                "UnitsInStock",
                "UnitsInOrder",
            ],
            logger=logger
        )

        exporter.export(file_type=args.type, filename=args.filename)