import sqlite3

def init_db(db_name: str, schema: str):
    connection = sqlite3.connect(db_name)

    with open(schema) as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()



# if __name__ == '__main__':
#     DATABASE = 'sqlite_db.db'
#     SCHEMA = 'schema.sql'
#     init_db(db_name=DATABASE, schema=SCHEMA)