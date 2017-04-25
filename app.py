import falcon
from Watson import messages
from Lex import client

api = application = falcon.API()

messages = messages.Message()

api.add_route('/watson/message', messages)

client = client.Messages()

api.add_route('/lex/message', client)
