import falcon
from Lex.client import Client

class Message(object):
    def __init__(self):
        self.client = Client()

    def on_post(self, req, resp):
        text = req.stream.read().decode('utf-8')
        message = self.client.post_text(text)
        resp.body = message
        resp.status = falcon.HTTP_200
