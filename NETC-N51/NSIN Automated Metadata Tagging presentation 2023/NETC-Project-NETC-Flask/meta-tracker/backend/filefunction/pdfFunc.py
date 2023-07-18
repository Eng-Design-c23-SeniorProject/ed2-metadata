from pymongo import MongoClient
import base64
import PyPDF2
import io
import openai
from bson import ObjectId

#MongoDB connection
client = MongoClient('mongodb+srv://guitryantenor:EBW2D4AV3zaDrx31@sthreeapp.dbfcmff.mongodb.net/?retryWrites=true&w=majority')
db = client['pdf_database']
collection = db['pdf_collection']

#OpenAI API key
openai.api_key = '#'

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

    #extract the summarized text from the API response
    summary = response.choices[0].text.strip()

    return summary
