from flask import Flask, request
from utils import read_file, get_fake_users, get_astronauts

app = Flask(__name__)

REQUIREMENTS = 'requirements.txt'


@app.route("/")
def hello_homework():
    return "Hello HomeWork"


@app.route('/requirements')
@app.route('/requirements/')
def requirements():
    """
        Read and return the contents of the 'requirements.txt' file.

        Returns:
            str: The contents of the 'requirements.txt' file with '<br>' HTML tags in place of line breaks.
    """
    return read_file(REQUIREMENTS)


@app.route('/generate-users')
def generate_users():
    """
        Generate a list of fake users and format it as an HTML string.

        Returns:
            str: A string containing the fake user information with '<br>' HTML tags separating each user.
    """
    quantity = request.args.get('quantity', "100")

    if quantity.isdigit():
        quantity = int(quantity)
        return get_fake_users(quantity)

    return f"Invalid query parameter <quantity>: {quantity}"


@app.route('/space')
@app.route('/space/')
def space():
    """
        Retrieve the number of astronauts currently in space and display it.

        Returns:
            str: A message indicating the total number of astronauts in Earth orbit.
    """
    total_astros = (get_astronauts()['number'])
    return f"A total number of astronauts on Earth's orbit are: {total_astros}"


if __name__ == '__main__':
    app.run(debug=True)
