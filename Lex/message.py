import falcon
from Lex.client import Client

class Message(object):
    def __init__(self):
        self.client = Client()

    def on_post(self, req, resp):
        message = self.client.post_text('I would like a pizza')
        resp.body = message
        resp.status = falcon.HTTP_200
