import falcon
import Watson.message
import Lex.message

api = application = falcon.API()

#lex routes
lex_message = Lex.message.Message()
api.add_route('/lex/message/', lex_message)

#watson routes
watson_message = Watson.message.Message()
api.add_route('/watson/message', watson_message)
