from mysql import connector
from app.database.config import Config
import sys
import csv



def export_db_to_csv(tables):
    mydb = connector.connect(
            host=Config.HOSTNAME,
            user=Config.USERNAME,
            password=Config.PASSWORD
        )
    mycursor = mydb.cursor()

    for table in tables:
        QUERY=f'SELECT * FROM mydbpaem.{table};'

        mycursor.execute(QUERY)
        result=mycursor.fetchall()

        c = csv.writer(open(f'{table}.csv', 'w'))
        for x in result:
            c.writerow(x)

    mydb.close()
    mycursor.close()

if __name__=="__main__":
    tables = ["usuario", "discente", "docente", "tecnico"]
    export_db_to_csv(tables)