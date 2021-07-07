from flask import Blueprint, Flask, render_template, request, url_for, redirect, session, jsonify
from flask.helpers import make_response
from flask.templating import render_template_string
import pymongo
import bcrypt
import json
import model.db



words_management_bp = Blueprint('words_management_bp', __name__,
    template_folder='templates')

client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db = client.get_database('total_records')
records = db.register

@words_management_bp.route("/", methods=['post', 'get'])
def index():
    if("email" in session):
        return render_template("words_index.html")
    else:
        return redirect(url_for("auth_bp.login"))

@words_management_bp.route("/getAll", methods=['GET'])
def getAll():
    if("email" in session):
        return make_response(getAllWordsJSON())
    else:
        return redirect(url_for("auth_bp.login"))

def getAllWordsJSON():
    return model.db.getAllWords()

@words_management_bp.route("/update", methods=['POST'])
def update():
    if("email" in session):
        return updateWord()
    else:
        return redirect(url_for("auth_bp.login"))

def updateWord():
    print(request.json)
    id = request.json["id"]
    word = request.json["word"]
    translation = request.json["translation"]
    collection = request.json["collection"]
    model.db.updateWord(id, word, translation, collection)
    return "true"

@words_management_bp.route("/delete/<id>", methods=["GET"])
def delete(id):
    if("email" in session):
            model.db.deleteWord(id)
            return ('', 204)
    else:
        return redirect(url_for("auth_bp.login"))
