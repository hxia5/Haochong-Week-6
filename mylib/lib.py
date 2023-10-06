"""
Extract a dataset from a URL

food dataset
"""
import requests
import sqlite3
import csv
import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def extract(url1="https://github.com/fivethirtyeight/data/blob/15f210532b2a642e85738ddefa7a2945d47e2585/world-cup-predictions/wc-20140609-140000.csv",
            url2="https://github.com/fivethirtyeight/data/blob/15f210532b2a642e85738ddefa7a2945d47e2585/world-cup-predictions/wc-20140613-205820.csv", 
            file_path1="dataset/wc-20140609-140000.csv", 
            file_path2="dataset/wc-20140613-205820.csv",
            directory="dataset"):
    """"Extract a url to a file path"""
    with requests.get(url1) as r:
        with open(file_path1, 'wb') as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, 'wb') as f:
            f.write(r.content)
    return file_path1, file_path2

"""
Transforms and Loads data into the local SQLite3 database
"""

#load the csv file and insert into a new sqlite3 database
def load(dataset1="dataset/wc-20140609-140000.csv",
        dataset2="dataset/wc-20140613-205820.csv"):
    """"Transforms and Loads data into the Databricks database"""
    df1 = pd.read_csv(dataset1, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    #prints the full working directory and path
    load_dotenv()
    host = os.getenv("SERVER_HOSTNAME")
    token = os.getenv("TOKEN")
    path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=host,
        access_token=token,
        http_path=path,
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'wc609'")
        result = c.fetchall() 
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS wc609 (
                    id int,
                    country string,
                    country_id string,
                    group string,
                    spi int,
                    spi_offense int,
                    spi_defense int,
                    win_group int,
                    sixteen int,
                    quarter int,
                    semi int,
                    cup int,
                    win int
                )
            """
            )
            for _, row in df1.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO wc609 VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'wc613'")
        result = c.fetchall() 
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS wc613 (
                    id int,
                    country string,
                    country_id string,
                    group string,
                    spi int,
                    spi_offense int,
                    spi_defense int,
                    win_group int,
                    sixteen int,
                    quarter int,
                    semi int,
                    cup int,
                    win int
                )
            """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO wc613 VALUES {convert}")
        c.close()
    return "success"

# save query record
qr = "query_record.md"


def save_qr(query, result="none"):
    """save in a markdown"""
    with open(qr, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")

"""Query the database"""

def complex_query():
    """do query by input"""
    load_dotenv()
    host = os.getenv("SERVER_HOSTNAME")
    token = os.getenv("TOKEN")
    path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=host,
        access_token=token,
        http_path=path,
    ) as connection:
        c = connection.cursor()
        c.execute("""SELECT t1.server, t1.opponent,
                AVG(spi) as avg_soccer_power_in_group,
                COUNT(win) as win_possibility
            FROM default.wc609 t1
            JOIN default.wc613 t2 ON t1.id = t2.id
            GROUP BY t1.group, t2.group
            ORDER BY win_possibility DESC
            LIMIT 3""")
        result = c.fetchall()

    save_qr("""SELECT t1.server, t1.opponent,
                AVG(spi) as avg_soccer_power_in_group,
                COUNT(win) as win_possibility
            FROM default.wc609 t1
            JOIN default.wc613 t2 ON t1.id = t2.id
            GROUP BY t1.group, t2.group
            ORDER BY win_possibility DESC
            LIMIT 3""", result)
