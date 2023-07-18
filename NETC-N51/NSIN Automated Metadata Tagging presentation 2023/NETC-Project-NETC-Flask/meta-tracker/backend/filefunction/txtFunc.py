from pymongo import MongoClient
import base64
import PyPDF2
import io
import openai
from bson import ObjectId
from flask import jsonify

# MongoDB connection
client = MongoClient('mongodb+srv://guitryantenor:EBW2D4AV3zaDrx31@sthreeapp.dbfcmff.mongodb.net/?retryWrites=true&w=majority')
db = client['text_database']
collection = db['text_collection']

#OpenAI API key
openai.api_key = '#'

# Function for storing text files
def store_text_file(file_data, filename):
    #Store the uploaded text file in MongoDB
    text_data = base64.b64encode(file_data).decode('utf-8')
    document = {'name': filename, 'data': text_data}
    collection.insert_one(document)

def extract_text_from_text_file(file_data):
    text_content = file_data
    return text_content

def summarize_text(text):
    #prompt for summarization
    prompt = "Summarize the following text in one paragraph:\n" + text

    #parameters for the summarization request from OpenAI
    parameters = {
        'engine': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 500,
        'temperature': 0.3,
        'top_p': 1.0,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0
    }

    #send summarization request to OpenAI API
    response = openai.Completion.create(**parameters)

    #extract the summarized text from the API response
    summary = response.choices[0].text.strip()

    return summary

