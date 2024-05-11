from flask import Flask
from flask_cors import CORS

from time import sleep

from db.characters import get_all_characters, get_character_by_id

app = Flask(__name__)
CORS(app)

@app.route("/characters")
def all_characters():
    return get_all_characters()

@app.route("/characters/<id>")
def character_by_id(id):
    sleep(1)
    return get_character_by_id(id)