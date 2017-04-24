import falcon
import messages

api = application = falcon.API()

messages = messages.Message()

api.add_route('/message', messages)
