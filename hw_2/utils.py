from faker import Faker
import requests


# -----------------------------------/requirements-------------------------------
def read_file(file: str) -> str:
    """
    Open and read a text file.

    Args:
        file (str): The path to the required text file.

    Returns:
        str: The contents of the file as a string with '<br>' HTML tags instead of line breaks.
    """

    with open(file, 'r') as f:
        lines = f.readlines()
        return "".join(lines).replace('\n', '<br>')


# -----------------------------/generate-users---------------------------------

def get_fake_users(amount: int = 100) -> str:
    """
    Generate a list of fake users, each with a name and an email, and format as an HTML string.

    Args:
        amount (int): The desired quantity of fake users. Default is 100.

    Returns:
        str: A string containing the fake user information with '<br>' HTML tags separating each user.
    """
    fake = Faker()
    list_with_users = [f"{fake.name()} : {fake.email()}" for _ in range(amount)]
    return "".join(map(lambda u: u + '<br>', list_with_users))


# -----------------------------/astros---------------------------------------
def get_astronauts() -> dict:
    """
    Retrieve JSON data from 'http://api.open-notify.org/astros.json' and parse it.

    Returns:
        dict: A dictionary representing the JSON data containing information about astronauts currently in space.
    """
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()


if __name__ == '__main__':
    print(read_file('requirements.txt'))
    print(get_fake_users(10))
    print(get_astronauts()['number'])
    print(type(get_astronauts()))
