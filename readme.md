# Recruitment tasks for Junior Python Developer

## Project overview
The project was created for the recruitment process for Hawatel. Given task could be described in list as follow:
1. Configure the mysql database **mydb** from given scripts [Schema](https://raw.githubusercontent.com/abdelatifsd/E-commerce-Database-Project/master/3%20-%20Structure.sql) and [Data](https://raw.githubusercontent.com/abdelatifsd/E-commerce-Database-Project/master/4%20-%20Population.sql).
2. Alter the product table with two additional columns **UnitPriceUSD** and **UnitPriceEuro**.
3. Create Python script to gather information from Polish National Bank REST API and update products data.
4. On demand script should also export list of all products to Excel format.

Other requirements:
- Script should be written in OOP
- Script should be documented
- Export altered database schema
- Script should use logging module
- Script should handle exceptions
- Optional: Script should be created in python packaging format to install the script with `pip install <module_name>.whl`

## Installation
- To create the database type `docker-compose up --build`
- To run the container type `docker-compose up`
- To run the container in the background type `docker-compose up -d`
- To stop the container type `docker-compose stop`
- To delete the database and it's volumes type `docker-compose down -v`




## Bugs Found
- In [Schema](https://raw.githubusercontent.com/abdelatifsd/E-commerce-Database-Project/master/3%20-%20Structure.sql) was mistype on check for Sellers Table which caused a check constraint violation while importing data for the sellers table.
```
...
CHECK (USER_TYPE = 'B'))
...
```
Should be this
```
...
CHECK (USER_TYPE = 'S'))
...
```