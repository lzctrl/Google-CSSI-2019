# main.py

import webapp2
import jinja2
import os
from models import Memes

from google.appengine.api import urlfetch
import json

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

meme_templates = ["https://i.imgflip.com/2/1ur9b0.jpg", "https://i.imgflip.com/2/1otk96.jpg", "https://i.imgflip.com/2/1g8my4.jpg",
"https://i.imgflip.com/2/1h7in3.jpg", "https://i.imgflip.com/2/grr.jpg", "https://i.imgflip.com/2/m78d.jpg",
"https://i.imgflip.com/2/1o00in.jpg", "https://i.imgflip.com/2/9ehk.jpg",
"https://i.imgflip.com/2/26am.jpg", "https://i.imgflip.com/2/1ihzfe.jpg",
"https://i.imgflip.com/2/2896ro.jpg", "https://i.imgflip.com/2/1w7ygt.jpg",
"https://i.imgflip.com/2/23ls.jpg", "https://i.imgflip.com/2/21uy0f.jpg",
"https://i.imgflip.com/2/2wifvo.jpg", "https://i.imgflip.com/2/1bgw.jpg",
"https://i.imgflip.com/2/261o3j.jpg", "https://i.imgflip.com/2/265k.jpg"]

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        api_url = "https://api.imgflip.com/get_memes"
        imgflip_response = urlfetch.fetch(api_url).content
        imgflip_response_json = json.loads(imgflip_response)
        meme_urls = []
        for meme_template in imgflip_response_json['data']['memes']:
            meme_urls.append(meme_template['url'])

        meme_dict = {
            "imgs": meme_urls
        }

        welcome_page = jinja_env.get_template('welcome.html')
        self.response.write(welcome_page.render(meme_dict))

class ResultPage(webapp2.RequestHandler):
    def post(self):
        top_line = self.request.get("top_line")
        bottom_line = self.request.get("bottom_line")
        meme_url = self.request.get("template")

        data_dict = {
            "top": top_line,
            "bottom": bottom_line,
            "url": meme_url
        }

        meme = Memes(top=top_line, bottom=bottom_line, imgURL=meme_url)
        meme.put()

        result_page = jinja_env.get_template('result.html')
        self.response.write(result_page.render(data_dict))

class AllMemesPage(webapp2.RequestHandler):
    def get(self):

        memes_query = Memes.query()

        all_memes = memes_query.fetch()
        print(all_memes)

        data_dict = {
            "memes": all_memes
        }

        print(data_dict)

        all_memes_page = jinja_env.get_template('allMemes.html')
        self.response.write(all_memes_page.render(data_dict))


# the app configuration section
app = webapp2.WSGIApplication(
    [('/', WelcomePage), ('/result', ResultPage), ('/allMemes', AllMemesPage)], debug = True
)
