import psycopg
from psycopg import OperationalError
import sys
sys.path.append('/workspace/sql-heroes')
from database.connection import create_connection,execute_query

# --------------------------- #
# --- READ HERO BIOGRAPHY --- #
# ----------------------------#

def read_bio(name):
    return execute_query(
    """
    SELECT name, biography
    FROM heroes
    WHERE name LIKE %s
    """,[name]
    ).fetchall()
    

result = read_bio('The Seer')
print(result)