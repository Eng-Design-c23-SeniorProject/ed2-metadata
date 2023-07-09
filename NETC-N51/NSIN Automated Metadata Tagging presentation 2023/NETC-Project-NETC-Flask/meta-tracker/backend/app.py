from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pymongo import MongoClient
import base64
import PyPDF2
import io
import openai
from bson import ObjectId

app = Flask(__name__)
CORS(app)

#MongoDB connection
client = MongoClient('#')
db = client['pdf_database']
collection = db['pdf_collection']

#OpenAI API key
openai.api_key = '#'

#files upload route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_data = file.read()

    #store the uploaded PDF file in MongoDB
    binary_data = base64.b64encode(file_data)
    document = {'name': file.filename, 'data': binary_data}
    collection.insert_one(document)

    return 'File uploaded successfully.'

#search route
@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    result = []

    #search for PDF files in the MongoDB collection
    for document in collection.find({'name': {'$regex': query, '$options': 'i'}}):
        result.append({'_id': str(document['_id']), 'name': document['name']})

    return jsonify(result=result, query=query)

#display route
@app.route('/display/<file_id>')
def display(file_id):
    document = collection.find_one({'_id': ObjectId(file_id)})
    if document is None:
        return 'File not found.'

    pdf_data = base64.b64decode(document['data'])

    #generate summary of the PDF file using OpenAI
    summary = summarize_pdf(pdf_data)

    response = {
        'pdfData': base64.b64encode(pdf_data).decode('utf-8'),
        'summary': summary
    }

    return jsonify(response)

#summary generator setup
def summarize_pdf(pdf_data):
    #extract text from the PDF file
    text_content = extract_text_from_pdf(pdf_data)

    #generate summary of the PDF file using OpenAI
    summary = summarize_text(text_content)

    return summary

#functions for text extraction and summarization
def extract_text_from_pdf(pdf_data):
    pdf_file = io.BytesIO(pdf_data)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    text_content = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text_content += page.extract_text()

    return text_content

def summarize_text(text):
    #prompt for summarization
    prompt = "Summarize the following text in one paragraph:\n" + text

    #parameters for the summarization request from OpenAI
    parameters = {
        'engine': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 100,
        'temperature': 0.3,
        'top_p': 1.0,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0
    }

    #send summarization request to OpenAI API
    response = openai.Completion.create(**parameters)

    #sxtract the summarized text from the API response
    summary = response.choices[0].text.strip()

    return summary

if __name__ == '__main__':
    app.run(debug=True)


#-----------------------------------------------------------------------------------------------
#implement upload,display, search and summarizzation functions for Docs, txt, image, video
#functions for dashboard and grammar check