import psycopg
import sys
sys.path.append('/workspace/sql-heroes/')
from database.connection import create_connection, execute_query

# -------------------- #
# --- ADD NEW HERO --- #
# ---------------------#

def create_hero(name,about,bio):
    execute_query("""
    INSERT INTO heroes (name,about_me,biography)
    VALUES (%s,%s,%s)
    """,[name,about,bio])
    print('New Hero added successfully!')


# create_hero('Pyro', 'Fire','I like Fire')