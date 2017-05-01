import falcon
from Lex.client import Client

class Message(object):
    def __init__(self):
        self.client = Client()

    def on_post(self, req, resp):
        #decode the incoming message
        text = req.stream.read().decode('utf-8')
        #ask lex what this message is
        message = self.client.post_message(text)
        print(message)
        #send back the message
        resp.body = message
        resp.status = falcon.HTTP_200
