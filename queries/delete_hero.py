import psycopg
import sys
sys.path.append('/workspace/sql-heroes/')
from database.connection import create_connection, execute_query

# ------------------- #
# --- DELETE HER0 --- #
# --------------------#
def delete_hero(name):
    execute_query(
    """ 
    DELETE FROM heroes
    WHERE name = %s
    """,[name]
    )
    print('Hero removed successfully!')