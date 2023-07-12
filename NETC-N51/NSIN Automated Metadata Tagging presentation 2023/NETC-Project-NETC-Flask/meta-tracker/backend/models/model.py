#MongoDB databse model to store the files
from mongoengine import Document, StringField, BinaryField
class PDFDocument(Document):
    name = StringField()
    data = BinaryField()

#add all models for files inside the route functions for now till deployment
#this file is currenttly not imported into any other files