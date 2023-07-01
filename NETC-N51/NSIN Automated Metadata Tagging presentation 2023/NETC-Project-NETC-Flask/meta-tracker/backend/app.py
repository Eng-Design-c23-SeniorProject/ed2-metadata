#app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import base64
import PyPDF2
import io
import openai
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient('#')
db = client['pdf_database']
collection = db['pdf_collection']

# OpenAI API key
openai.api_key = '#'

# File upload route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_data = file.read()

    # Store the uploaded PDF file in MongoDB
    pdf_data = base64.b64encode(file_data).decode('utf-8')
    name = file.filename
    document = {'name': name, 'data': pdf_data}
    collection.insert_one(document)

    return 'File uploaded successfully.'

# Search route
@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    result = []

    # Search for PDF files in the MongoDB collection
    for document in collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

# Display route
@app.route('/display/<file_id>')
def display(file_id):
    document = collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return 'File not found.'

    pdf_data = base64.b64decode(document['data'])
    text_content = extract_text_from_pdf(pdf_data)

    # Generate summary of the PDF file using OpenAI
    summary = summarize_pdf(text_content)

    return jsonify(text_content=text_content, summary=summary)

# Help functions for text extraction and summarization
def extract_text_from_pdf(pdf_data):
    pdf_file = io.BytesIO(pdf_data)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    text_content = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text_content += page.extract_text()

    return text_content

def summarize_pdf(text):
    # Prompt for summarization
    prompt = "Summarize the following text:\n" + text

    # Parameters for the summarization request
    parameters = {
        'engine': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 100,
        'temperature': 0.3,
        'top_p': 1.0,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0
    }

    # Send summarization request to OpenAI API
    response = openai.Completion.create(**parameters)

    # Extract the summarized text from the API response
    summary = response.choices[0].text.strip()

    return summary

if __name__ == '__main__':
    app.run(debug=True)