#MongoDB databse model to store the files
from mongoengine import Document, StringField, BinaryField

class PDFDocument(Document):
    name = StringField()
    data = BinaryField()


'''add models for Docs, txt, image, video files'''

class TxtDocument(Document):
    name = StringField()
    data = BinaryField()

class DocDocument(Document):
    name = StringField()
    data = BinaryField()