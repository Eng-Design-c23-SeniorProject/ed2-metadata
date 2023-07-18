#imgFunc.py
from pymongo import MongoClient
import base64
from bson import ObjectId
import io

#MongoDB connection
client = MongoClient('mongodb+srv://guitryantenor:EBW2D4AV3zaDrx31@sthreeapp.dbfcmff.mongodb.net/?retryWrites=true&w=majority')
db = client['img_database']
collection = db['img_collection']

#functions for image handling
def store_image(file_data, filename):
    #store the uploaded image file in MongoDB
    binary_data = base64.b64encode(file_data)
    document = {'name': filename, 'data': binary_data}  #database model
    collection.insert_one(document)

def get_image(file_id):
    document = collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return None

    image_data = base64.b64decode(document['data'])
    return image_data

def search_images(query):
    result = []

    #search for image files in the MongoDB collection
    for document in collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return result