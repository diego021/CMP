#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.CMP

def insert(collection: str, data: dict) -> None:
    collection = getattr(db, collection)
    collection.insert_one(data)

def find_local_track(filename):
    collection = getattr(db, 'library')
    try:
        document = collection.find({'filename': filename})[0]
    except IndexError:
        return False
    else:
        return document

