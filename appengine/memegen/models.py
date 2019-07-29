from google.appengine.ext import ndb

class Memes(ndb.Model):
    top = ndb.StringProperty(required=True)
    bottom = ndb.StringProperty(required=True)
    imgURL = ndb.StringProperty(required=True)
