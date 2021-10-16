from mysql import connector
from app.database.config import Config
import sys
import csv



def export_db_to_csv(tables):
    mydb = connector.connect(
            host=Config.HOSTNAME,
            user=Config.USERNAME,
            password=Config.PASSWORD,
            charset='utf8'
        )
    mycursor = mydb.cursor()

    for table in tables:
        QUERY=f'SELECT * FROM mydbpaem.{table};'

        mycursor.execute(QUERY)
        result=mycursor.fetchall()
        columns_name=[desc[0] for desc in mycursor.description]
        print(f"### data from table {table} ###")
        print(columns_name)
        with open(f'app/database/inputs/{table}.csv', 'w') as f:
            c = csv.writer(f)
            c.writerow(columns_name)
            for x in result:
                c.writerow(x)

    mydb.close()
    mycursor.close()

if __name__=="__main__":
    columns_dict = {
        "usuario":[], "discente":[], 
        "docente":[], "tecnico":[], 
        "recurso_campus":[], "campus_instituto":[],
        "acesso_permitido":[], "solicitacao_acesso":[],
        "curso":[], "disciplina":[],
        "protocolo":[]
        }

    tables = [
        "usuario", "discente", 
        "docente", "tecnico", 
        "recurso_campus", "campus_instituto",
        "acesso_permitido", "solicitacao_acesso",
        "curso", "disciplina",
        "protocolo"
    ]
    export_db_to_csv(tables)