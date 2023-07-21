from pymongo import MongoClient
import base64
import io
import openai
import docx

#MongoDB connection
client = MongoClient('mongodb+srv://guitryantenor:EBW2D4AV3zaDrx31@sthreeapp.dbfcmff.mongodb.net/?retryWrites=true&w=majority')
db = client['doc_database']
collection = db['doc_collection']

#OpenAI API key
openai.api_key = '#'

#functions for text extraction and summarization
def extract_text_from_doc(doc_data):
    doc = docx.Document(io.BytesIO(doc_data))
    text_content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
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
    #sending summarization request to OpenAI API
    response = openai.Completion.create(**parameters)

    #extracting the summarized text from the API response
    summary = response.choices[0].text.strip()

    return summary
