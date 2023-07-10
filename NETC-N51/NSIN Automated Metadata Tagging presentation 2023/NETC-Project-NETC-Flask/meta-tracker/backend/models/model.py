#MongoDB databse model to store the files
from mongoengine import Document, StringField, BinaryField
#Alex models
class PDFDocument(Document):
    name = StringField()
    data = BinaryField()

#cesar models   --add and edit as needed
class TxtDocument(Document):
    name = StringField()
    data = BinaryField()

#Garrett models  --add and edit as needs
class DocDocument(Document):
    name = StringField()
    data = BinaryField()