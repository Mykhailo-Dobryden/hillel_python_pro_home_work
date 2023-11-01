import sqlite3

def init_db(db_name: str, schema: str):
    """
        Initializes an SQLite database by creating tables and executing the schema definition.

        Args:
            db_name (str): The name of the SQLite database to be initialized.
            schema (str): The path to the schema file containing SQL script for creating a table.

        This function creates an SQLite database with the specified name and executes the SQL script defined in the provided schema file.
        The schema file typically contains table creation and schema definitions. After executing the script,
        the function commits the changes and closes the database connection.

        Note: Make sure to pass the correct paths to the database name and schema file.
    """
    connection = sqlite3.connect(db_name)

    with open(schema) as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()



# if __name__ == '__main__':
#     DATABASE = 'sqlite_db.db'
#     SCHEMA = 'schema.sql'
#     init_db(db_name=DATABASE, schema=SCHEMA)