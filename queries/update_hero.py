import psycopg
import sys
sys.path.append('/workspace/sql-heroes/')
from database.connection import create_connection, execute_query

# ------------------- #
# --- UPDATE HERO --- #
# --------------------#
def update_bio(bio, name):
    update = execute_query(""" 
    UPDATE heroes
    SET biography = %s
    WHERE NAME = %s
    """, [bio, name]
    )
    return update
    print('You have successfully updated the biography')