#MongoDB databse model to store the files
from mongoengine import Document, StringField, BinaryField, FileField
class PDFDocument(Document):
    name = StringField()
    data = BinaryField()

class TextFile(Document):
    name = StringField()
    data = BinaryField()

class VideoFile(Document):
    name = StringField()
    filedata = FileField()

#add all models for files inside the route functions for now till deployment
#this file is currenttly not imported into any other files

#currently not in use and need to be re-routing