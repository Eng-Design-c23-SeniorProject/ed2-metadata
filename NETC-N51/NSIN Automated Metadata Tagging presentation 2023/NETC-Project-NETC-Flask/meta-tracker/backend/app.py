#app.py
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import base64
import io
from bson import ObjectId
#from models.model import TextFile, VideoFile
from mongoengine import connect, Document, StringField, FileField
from filefunction.pdfFunc import extract_text_from_pdf, summarize_text, collection as pdf_collection
from filefunction.imgFunc import store_image, get_image, search_images, collection as img_collection
from filefunction.videoFunc import collection as video_collection, store_video, retrieve_video_data
from filefunction.txtFunc import collection as text_collection, store_text_file
from filefunction.docsFunc import extract_text_from_doc, summarize_text, collection as doc_collection

app = Flask(__name__)
CORS(app)

#PDF upload route
@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    file_data = file.read()

    # Store the uploaded PDF file in MongoDB
    binary_data = base64.b64encode(file_data)
    document = {'name': file.filename, 'data': binary_data}  # Database model
    pdf_collection.insert_one(document)

    return 'PDF file uploaded successfully.'

#PDF search route
@app.route('/search-pdf', methods=['POST'])
def search_pdf():
    query = request.json['query']
    result = []

    #search for PDF files in the MongoDB collection
    for document in pdf_collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

#PDF display route
@app.route('/display-pdf/<file_id>')
def display_pdf(file_id):
    document = pdf_collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return 'PDF file not found.'

    pdf_data = base64.b64decode(document['data'])

    #generate summary of the PDF file using OpenAI
    summary = summarize_text(extract_text_from_pdf(pdf_data))

    response = {
        'pdfData': base64.b64encode(pdf_data).decode('utf-8'),
        'summary': summary
    }

    return jsonify(response)

#image upload route
@app.route('/upload-image', methods=['POST'])
def upload_image():
    file = request.files['image']
    file_data = file.read()
    filename = file.filename

    #storing the uploaded image file in MongoDB
    store_image(file_data, filename)

    return 'Image uploaded successfully.'

#image search route
@app.route('/search-image', methods=['POST'])
def search_image():
    query = request.json['query']

    #searching for image files in the MongoDB collection
    result = search_images(query)

    return jsonify(result=result, query=query)

#image display route
@app.route('/display-image/<file_id>')
def display_image(file_id):
    image_data = get_image(file_id)
    if image_data is None:
        return 'Image not found.', 404

    #instead of sending the raw image data as bytes, let's send it as a response
    return send_file(io.BytesIO(image_data), mimetype='image/jpeg')

#text upload route
@app.route('/upload-text', methods=['POST'])
def upload_text():
    file = request.files['file']
    file_data = file.read()
    filename = file.filename

    #storing the uploaded text file in MongoDB
    store_text_file(file_data, filename)

    return 'Text file uploaded successfully.'

#text search route
@app.route('/search-text', methods=['POST'])
def search_text():
    query = request.json['query']
    result = []

    #searching for files in the MongoDB collection
    for document in text_collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

#extracting text files from mongoDB
def extract_text_from_mongodb(file_id):
    document = text_collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return None

    text_data = document['data']
    return text_data

#text display route
@app.route('/display-text/<file_id>')
def display_text(file_id):
    text_data = extract_text_from_mongodb(file_id)
    if text_data is None:
        return jsonify({'error': 'Text file not found.'}), 404

    #generating summary of the text data using OpenAI
    summary = summarize_text(text_data)

    response = {
        'textData': text_data,
        'summary': summary
    }

    return jsonify(response)

#video upload routing
@app.route('/upload-video', methods=['POST'])
def upload_video():
    file = request.files['video']
    file_data = file.read()
    filename = file.filename

    #storing the uploaded video file in MongoDB
    store_video(file_data, filename)

    return 'Video uploaded successfully.'

#video search route
@app.route('/search-video', methods=['POST'])
def search_video():
    query = request.json['query']
    result = []

    #searching for files in the MongoDB collection
    for document in video_collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

#video display route
@app.route('/display-video/<file_id>')
def display_video(file_id):
    #retrieving the video data
    video_data = retrieve_video_data(file_id)
    if video_data is None:
        return 'Video not found.'

    #sending the video data as a response
    return send_file(video_data, mimetype='video/mp4')

#docx upload route
@app.route('/upload-doc', methods=['POST'])
def upload_doc():
    file = request.files['file']
    file_data = file.read()

    #storing the uploaded docx file in MongoDB
    binary_data = base64.b64encode(file_data)
    document = {'name': file.filename, 'data': binary_data}  # Database model
    doc_collection.insert_one(document)

    return 'DOC file uploaded successfully.'

#docx search route
@app.route('/search-doc', methods=['POST'])
def search_doc():
    query = request.json['query']
    result = []

    #searching for docx files in the MongoDB collection
    for document in doc_collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

#docx display route
@app.route('/display-doc/<file_id>')
def display_doc(file_id):
    document = doc_collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return 'DOC file not found.'

    doc_data = base64.b64decode(document['data'])

    #generating summary of the docx file using OpenAI
    summary = summarize_text(extract_text_from_doc(doc_data))

    response = {
        'docData': base64.b64encode(doc_data).decode('utf-8'),
        'summary': summary
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)