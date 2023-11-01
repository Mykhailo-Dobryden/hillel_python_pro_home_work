def generate_phones_update_query(phone_id: str, name: str = None, phone: int = None) -> str:
    """
    Generates an SQL query to update a record in the 'phones' table based on the provided parameters.

    Args:
        phone_id (str): The unique identifier (a number) of the phone record to update.
        name (str, optional): The new name to assign to the contact. If None, the name won't be updated.
        phone (int, optional): The new phone number value to assign to the contact.
                If None, the phone number won't be updated.

    Returns:
        str: An SQL query string that can be executed to update the specified phone record in the 'phones' table.
    """
    args = {'contactName': f"'{name}'", 'phoneValue': phone}
    set_clause = ", ".join([f"{k} = {v}" for k, v in args.items() if v is not None])
    sql_query = f"""UPDATE phones
                    SET {set_clause}
                    WHERE phoneID = {phone_id}"""
    return sql_query


def generate_phones_delete_query(phone_id: str) -> str:
    """
    Generates an SQL query to delete a phone record from the 'phones' table based on the provided phone ID.

    Args:
        phone_id (str): The unique identifier of the phone record to delete.

    Returns:
        str: An SQL query string that can be executed to delete the specified phone record from the 'phones' table.
    """
    return f"""DELETE FROM phones WHERE phoneID = {phone_id}"""


def generate_phones_read_query(order: str = 'id') -> str:
    """
    Generates an SQL query to read phone records from the 'phones' table with an optional specified order.

    Args:
        order (str, optional): The order by which the phone records should be retrieved. Defaults to 'id'.
            Possible values for order:
                - 'id': Orders by phone ID (default).
                - 'name': Orders by contact name.
                - 'phone': Orders by phone number value.

    Returns:
        str: An SQL query string that can be executed to retrieve phone records from the 'phones' table, ordered as specified.
    """
    ords = {'id': 'phoneID',
            'name': 'contactName',
            'phone': 'phoneValue'}
    return f"SELECT * FROM phones ORDER BY {ords.get(order, 'phoneID')}"


def generate_phones_create_query(name: str, phone: str) -> str:
    """
    Generates an SQL query to create a new phone record in the 'phones' table.

    Args:
        name (str): The contact name to associate with the new phone record.
        phone (str): The phone number value to associate with the new phone record.

    Returns:
        str: An SQL query string that can be executed to insert a new phone record into the 'phones' table.
    """
    return f"""INSERT INTO phones (contactName, phoneValue) 
                    VALUES ('{name}', {phone})"""
