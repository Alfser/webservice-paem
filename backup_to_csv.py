from mysql import connector
from app.database.config import Config
import os
import pandas as pd



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
        df_result = pd.DataFrame(data=result, columns=columns_name)
        csv_path = f'app/database/inputs/{table}.csv'
        abs_csv_path = os.path.abspath(csv_path)
        print("abs path:", abs_csv_path)
        df_result.to_csv(abs_csv_path, encoding="UTF-8", index=False, sep=";")
        
    mydb.close()
    mycursor.close()

if __name__=="__main__":
    
    tables = [
        "usuario", "discente", 
        "docente", "tecnico", 
        "recurso_campus", "campus_instituto",
        "acesso_permitido", "solicitacao_acesso",
        "curso", "disciplina",
        "protocolo"
    ]
    export_db_to_csv(tables)