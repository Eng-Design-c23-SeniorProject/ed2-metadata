from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import base64
import io
from bson import ObjectId
from filefunction.pdfFunc import extract_text_from_pdf, summarize_text, collection as pdf_collection
from filefunction.imgFunc import store_image, get_image, search_images, collection as image_collection
#from models.model import TextFile, VideoFile
from mongoengine import connect, Document, StringField, FileField
from filefunction.videoFunc import collection as video_collection, store_video, retrieve_video_data
from filefunction.txtFunc import collection as text_collection, store_text_file

app = Flask(__name__)
CORS(app)

# PDF upload route
@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    file_data = file.read()

    # Store the uploaded PDF file in MongoDB
    binary_data = base64.b64encode(file_data)
    document = {'name': file.filename, 'data': binary_data}  # Database model
    pdf_collection.insert_one(document)

    return 'PDF file uploaded successfully.'

# PDF search route
@app.route('/search-pdf', methods=['POST'])
def search_pdf():
    query = request.json['query']
    result = []

    # Search for PDF files in the MongoDB collection
    for document in pdf_collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

# PDF display route
@app.route('/display-pdf/<file_id>')
def display_pdf(file_id):
    document = pdf_collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return 'PDF file not found.'

    pdf_data = base64.b64decode(document['data'])

    # Generate summary of the PDF file using OpenAI
    summary = summarize_text(extract_text_from_pdf(pdf_data))

    response = {
        'pdfData': base64.b64encode(pdf_data).decode('utf-8'),
        'summary': summary
    }

    return jsonify(response)

# Image upload route
@app.route('/upload-image', methods=['POST'])
def upload_image():
    file = request.files['image']
    file_data = file.read()
    filename = file.filename

    # Store the uploaded image file in MongoDB
    store_image(file_data, filename)

    return 'Image uploaded successfully.'

# Image search route
@app.route('/search-image', methods=['POST'])
def search_image():
    query = request.json['query']

    # Search for image files in the MongoDB collection
    result = search_images(query)

    return jsonify(result=result, query=query)

# Image display route
@app.route('/display-image/<file_id>')
def display_image(file_id):
    image_data = get_image(file_id)
    if image_data is None:
        return 'Image not found.'

    # Send the image data as a response
    return send_file(base64.b64encode(image_data), mimetype='image/jpeg')

#
#txt files routing
#add all models for files inside the route functions for now till deployment
#
# Text upload route
@app.route('/upload-text', methods=['POST'])
def upload_text():
    file = request.files['file']
    file_data = file.read()
    filename = file.filename

    # Store the uploaded text file in MongoDB
    store_text_file(file_data, filename)

    return 'Text file uploaded successfully.'

# Text Search Route
@app.route('/search-text', methods=['POST'])
def search_text():
    query = request.json['query']
    result = []

    # Search for files in the MongoDB collection
    for document in text_collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

#extracts text files from mongo
def extract_text_from_mongodb(file_id):
    document = text_collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return None

    text_data = document['data']
    return text_data

# Text display route
@app.route('/display-text/<file_id>')
def display_text(file_id):
    text_data = extract_text_from_mongodb(file_id)
    if text_data is None:
        return jsonify({'error': 'Text file not found.'}), 404

    # Generate summary of the text data using OpenAI
    summary = summarize_text(text_data)

    response = {
        'textData': text_data,
        'summary': summary
    }

    return jsonify(response)

#video files routing
#add all models for files inside the route functions for now till deployment

@app.route('/upload-video', methods=['POST'])
def upload_video():
    file = request.files['video']
    file_data = file.read()
    filename = file.filename

    # Store the uploaded video file in MongoDB
    store_video(file_data, filename)

    return 'Video uploaded successfully.'

# Video Search Route
@app.route('/search-video', methods=['POST'])
def search_video():
    query = request.json['query']
    result = []

    # Search for files in the MongoDB collection
    for document in video_collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

# Video display route
@app.route('/display-video/<file_id>')
def display_video(file_id):
    # Retrieve the video data
    video_data = retrieve_video_data(file_id)
    if video_data is None:
        return 'Video not found.'

    # Send the video data as a response
    return send_file(video_data, mimetype='video/mp4')

#
#docs files routing and models

#add all models for files inside the route functions for now till deployment
#

if __name__ == '__main__':
    app.run(debug=True)