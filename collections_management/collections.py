from flask import Blueprint, Flask, render_template, request, url_for, redirect, session
from flask.helpers import make_response
from flask.templating import render_template_string
import pymongo
import bcrypt
import model.db


collections_bp = Blueprint('collections_bp', __name__,
    template_folder='templates')

@collections_bp.route("/", methods=['post', 'get'])
def index():
    if("email" in session):
        return render_template("collections_index.html")
    else:
        return redirect(url_for("auth_bp.login"))

@collections_bp.route("/get", methods=['get'])
def getAll():
    if "email" not in session:
        return redirect(url_for("auth_bp.login"))
    collections = model.db.getAllCollections()
    return collections

@collections_bp.route("/add", methods=["post"])
def add():
    if "email" not in session:
        return redirect(url_for("auth_bp.login"))
    model.db.addCollection(request.json["name"], session["email"])
    return "true"

@collections_bp.route("/edit", methods=["post"])
def edit():
    pass

@collections_bp.route("/remove", methods=["get"])
def remove(id):
    pass