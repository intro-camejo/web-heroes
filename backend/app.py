from flask import Flask
from flask_cors import CORS

from time import sleep

from db.characters import get_all_characters, get_character_by_id, remove_character

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return """
    <html>
    <body>
    <h1>Welcome to my heroes API</h1>
    <a href="/characters">Go to all characters</a>
    </body>
    </html>
    """

@app.route("/characters")
def all_characters():
    return get_all_characters()

@app.route("/characters/<id>")
def character_by_id(id):
    sleep(1)
    return get_character_by_id(id)

@app.route("/characters/<id>", methods = ["DELETE"])
def remove_character_by_id(id):
    return {"success": remove_character(id)}
