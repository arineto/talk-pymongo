from bson.objectid import ObjectId
from pymongo import MongoClient


client = MongoClient()
db = client.get_database('talk_pymongo')


def create(collection_name, data):
    collection = db.get_collection(collection_name)
    created = collection.insert(data)
    return str(created)


def retrieve(collection_name, filters={}):
    collection = db.get_collection(collection_name)
    return collection.find(filters)


def update(collection_name, mongo_id, data):
    collection = db.get_collection(collection_name)
    collection.update(
        {'_id': ObjectId(mongo_id)},
        {'$set': data}
    )
    return mongo_id


def delete(collection_name, mongo_id):
    collection = db.get_collection(collection_name)
    collection.remove({'_id': ObjectId(mongo_id)})
    return mongo_id
