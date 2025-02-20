

"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime

# Opens a connection to an SQLite database.
# Returns a Connection object that represent the database connection.
# A new database file will be created if it doesn't already exist.
con = sqlite3.connect('social_network.db')

cur = con.cursor()
# Define an SQL query that creates a table named 'people'.
# Each row in this table will hold information about a specific person.
create_ppl_tbl_query = """
CREATE TABLE IF NOT EXISTS people
(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
email TEXT NOT NULL,
address TEXT NOT NULL,
city TEXT NOT NULL,
province TEXT NOT NULL,
bio TEXT,
age INTEGER,
created_at DATETIME NOT NULL,
updated_at DATETIME NOT NULL
);
"""
# Execute the SQL query to create the 'people' table.
# Database operations like this are called transactions.
cur.execute(create_ppl_tbl_query)
# Commit (save) pending transactions to the database.
# Transactions must be committed to be persistent.
con.commit()
# Close the database connection.
# Pending transactions are not implicitly committed, so any
# pending transactions that have not been committed will be lost.
con.close()







# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    return

if __name__ == '__main__':
   main()