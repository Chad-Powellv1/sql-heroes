import psycopg
from psycopg.rows import dict_row
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        conn = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            row_factory=dict_row,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return conn




def execute_query(query,params):
    conn = create_connection('postgres', 'postgres', 'postgres')
    cursor = conn.cursor()
    try:
        cursor.execute(query,params)
        conn.commit()
        print("Query executed successfully")
        return cursor
    except OperationalError as e:
        print(f"The error '{e}' occurred")