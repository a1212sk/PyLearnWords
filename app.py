

from flask import Flask
from auth.auth import auth_bp
from words_management.words import words_management_bp
from collections_management.collections import collections_bp

app = Flask(__name__)
app.secret_key = "testing"

app.register_blueprint(auth_bp,url_prefix="/")
app.register_blueprint(words_management_bp, url_prefix="/words")
app.register_blueprint(collections_bp, url_prefix="/collections")


if __name__ == "__main__":
  app.run(debug=True)
