import psycopg
from psycopg import OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    try:
        connection = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(query):
    # Connect to an existing database
    with create_connection("postgres", "postgres", "postgres") as conn:
       cur = connection.cursor()
       try:
            cur.execute(query)
            conn.committ()
            print("Query executed successfully")
            return cur
        except Error as e:
            print(f"The error as '{e}'occurred or the hero name is already taken!")
