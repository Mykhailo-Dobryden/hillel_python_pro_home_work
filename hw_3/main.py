from flask import Flask, request, render_template
import sqlite3
import os
from inint_db import init_db
from utils import generate_phones_update_query, generate_phones_delete_query, generate_phones_read_query, \
    generate_phones_create_query

app = Flask(__name__)

DATABASE = 'sqlite_db.db'
SCHEMA = 'schema.sql'

import sqlite3

def get_db_connection():
    """
    Establishes a connection to the SQLite database defined by the constant DATABASE and configures
    it for row-based data access.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn



@app.route("/phones/create", methods=["POST", "GET"])
def phones_create():
    """
        Handles the creation of a new phone record in the database based on the data provided
        via a POST or GET request.

        This route function expects two parameters, 'name' and 'phone', to create a new phone record.
        It validates the input data and, if valid, generates an SQL query to insert the new phone record into the database.
         After the record is inserted, the function returns a success message.

        Returns:
            str: A success message if the phone record is added successfully, or an error message if validation fails.
    """

    contact_name = request.args.get('name')
    phone_value = request.args.get('phone')

    if not contact_name:
        return 'name is required!'
    elif not contact_name.isalpha():
        return 'name must consist of letters'
    elif not phone_value:
        return 'phone number is required!'
    elif not phone_value.isdigit():
        return 'phone number must consist only digits'
    else:
        sql_query = generate_phones_create_query(name=contact_name, phone=phone_value)
        with get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql_query)
            conn.commit()

    return 'Phone was added'


@app.route("/phones/read")
def phones_read():
    """
        Retrieves and displays phone records from the database, with optional sorting based on the 'order' parameter.
            Possible values for order:
                - 'id': Orders by phone ID (default).
                - 'name': Orders by contact name.
                - 'phone': Orders by phone number value.

        It renders an HTML template to display the records.

        Returns:
            str: An HTML template displaying phone records or an error message if the 'order' parameter is missing.
    """
    order = request.args.get('order')
    if not order:
        return "Use 'order' for sorting data by next colum: id, name, phone"

    with get_db_connection() as conn:
        cur = conn.cursor()
        sql_query = generate_phones_read_query(order)
        phones = cur.execute(sql_query).fetchall()

    return render_template('phones_read.html', phones=phones)


@app.route("/phones/update")
def phones_update():
    """
        Handles the update of a phone record in the database based on the provided parameters.

        This route function allows updating a phone record in the database by specifying the
        phone record's 'id', 'name', and 'phone' parameters. The 'id' parameter is required,
        and either 'name' or 'phone' or both are also required for the update to take place.

        Returns:
            str: A success message if the phone record is updated, or an error message if required parameters are missing.
    """
    phone_id = request.args.get('id')
    contact_name = request.args.get('name')
    phone_value = request.args.get('phone')

    if phone_id is None:
        return 'id is required!'
    if not contact_name and not phone_value:
        return "Either [name] or [phone], or both are required!"

    sql_query = generate_phones_update_query(phone_id=phone_id, name=contact_name, phone=phone_value)

    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute(sql_query)
        conn.commit()

    return f"Phone with id '{phone_id}' was updated, if it had been in database before then))))"


@app.route("/phones/delete")
def phones_delete():
    """
        Handles the deletion of a phone record from the database based on the provided phone ID.

        This route function allows deleting a phone record from the database by specifying the
        phone record's 'id' parameter, which is required.

        Returns:
            str: A success message if the phone record is deleted, or
            an error message if the 'id' parameter is missing.
    """
    phone_id = request.args.get('id')
    if phone_id is None:
        return 'id is required!'

    sql_request = generate_phones_delete_query(phone_id)

    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute(sql_request)
        conn.commit()

    return f"Phone with phoneID '{phone_id}' was deleted, if it had been in database before then:))))"


# ------------------------ create database if it doesnt exists----------------

if DATABASE not in os.listdir():
    print("not in os.listdir")
    init_db(db_name=DATABASE, schema=SCHEMA)
else:
    print('is in os.listdr')
    print(os.listdir())

# --------------------------------if name is main-------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
