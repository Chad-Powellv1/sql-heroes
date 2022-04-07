import psycopg
import sys
sys.path.append('/workspace/sql-heroes1')
from database.connection import create_connection, execute_query

def small_journey():
    print(""" 
# ---------------------------------------------------------------#
# ------------------------ INITIALIZING ------------------------ #
# ---------------------------------------------------------------#

    \n Welcome to the Super Heroes information network. 🦸
    \n How would you like to interact with the network? 
    \n
    1. Create a super hero
    2. Read about a super hero
    3. Update the super hero's biography
    4. Delete a super hero
    5. Exit

    Enter the number: 
    """
    )
    num = input()
    if num == 1:
        create_hero(name,about,bio)


small_journey()
