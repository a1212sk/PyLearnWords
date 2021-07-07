from bson.objectid import ObjectId
from flask import Blueprint, Flask, render_template, request, session, jsonify
import pymongo
import bcrypt
import json

client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db = client.get_database('total_records')
records = db.register

# words #####################################################
def updateWord(id, word, translation, collection):
    """Insert/Update a new word to the db"""

    objId = ObjectId(id)
    db.words.update_one({"_id":objId},{"$set":{
        "word":word,
        "translation":translation,
        "collection":collection
    }}, upsert=True)

def deleteWord(id):
    db.words.delete_one({"_id":ObjectId(id)})

def getAllWords(collectionId='all'):
    words = db.words.find({"collection": collectionId})
    return json.dumps(list(words), default=str)

##############################################################

# collections ################################################

def getAllCollections():
    collections = db.collections.find({"$or":[{"userId": session["email"]}, {"userId": "all"}]})
    return json.dumps(list(collections), default=str)

def addCollection(name, userId):
    db.collections.insert_one({"_id":ObjectId(), "name":name, "userId":userId})

def removeCollection(id):
    db.collections.delete_one({"$and":[{"_id":ObjectId(id)}, {"userId":{"$ne":"all"}}]})

##############################################################
