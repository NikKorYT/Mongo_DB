from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    ListField,
    StringField,
    ReferenceField
)


class authors(Document):
    full_name = StringField(required=True)
    born_date = DateTimeField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)
    
class qoutes(Document):
    tags = ListField(StringField())
    author = ReferenceField(authors)
    qoute = StringField(required=True)
    

