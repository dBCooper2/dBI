import sqlite3
import pandas as pd

class ProjectDatabase:
    def __init__(self, db_name: str) -> None:
        # Connect to SQLite database (or create a new one if it doesn't exist)
        self.conn = sqlite3.connect(db_name)

        # Create a cursor object
        self.cursor = self.conn.cursor()

        # Define the SQL query to create a table
        with open('schema.sql', 'r') as file:
            create_table_query = file.read()

        # Execute the query to create the table
        self.cursor.execute(create_table_query)
        
    def append_data(self, table_name: str, data: pd.DataFrame):
        data.to_sql(table_name, self.conn, index=False, if_exists='append')

    def replace_data(self, table_name: str, data: pd.DataFrame):
        data.to_sql(table_name, self.conn, index=False, if_exists='replace')

    def commit_changes(self):
        # Commit the changes
        self.conn.commit()

    def close_db(self):
        # Close the connection
        self.conn.close()
