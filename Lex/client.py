import boto3
import uuid
from Lex.constants import BOT_NAME, BOT_ALIAS, LEX_RUNTIME

class Client(object):
    def __init__(self):
        self.user_id = uuid.uuid4()
        self.boto = boto3.client(LEX_RUNTIME)

    def post_text(self, text):
        response = self.boto.post_text(botName=BOT_NAME, botAlias=BOT_ALIAS, userId=str(self.user_id), inputText=text)
        if response['message'] is not None:
            return response['message']
