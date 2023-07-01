#model.py

#MongoDB databse model to store the files
from mongoengine import Document, StringField, BinaryField

class PDFDocument(Document):
    name = StringField()
    data = BinaryField()