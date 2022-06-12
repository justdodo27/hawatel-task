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
- Export [altered database schema](https://github.com/justdodo27/hawatel-task/blob/main/AlteredStructure.sql)
- Script should use logging module
- Script should handle exceptions
- Optional: Script should be created in python packaging format to install the script with `pip install <module_name>.whl`

## Installation

### Database
- To create the database type `docker-compose up --build`
- To run the container type `docker-compose up`
- To run the container in the background type `docker-compose up -d`
- To stop the container type `docker-compose stop`
- To delete the database and it's volumes type `docker-compose down -v`
- To open mysql shell type `docker-compose exec mysql /bin/bash` while the container is running and after that type `mysql -u user -puser`

### Python Script
- Create virtual environment `python3 -m venv venv`
- Change virtual environment `source venv/bin/activate`
- Install required packages `pip3 install -r requirements.txt`
- Run script with `python3 script.py`

## Script options

- -h, --help

show help message and exit
- --host HOST

set database host, default 127.0.0.1
- --user USER, -u USER

set database user, default user
- --password PASSWORD, -p PASSWORD

set database password, default user
- --db DB

set database name, default mydb
- --export, --no-export, -e

exports data from database to external file
- --type TYPE

set export file format, default excel
- --filename FILENAME

set export filename, default ./export
- --log_path LOG_PATH

set log path, default ./


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