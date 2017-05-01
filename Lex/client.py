import boto3
import uuid
from Lex.constants import BOT_NAME, BOT_ALIAS, LEX_RUNTIME
from Lex.intent import Intent
from GoogleCalendar.calendar import Calendar

class Client(object):
    def __init__(self):
        self.user_id = uuid.uuid4()
        self.boto = boto3.client(LEX_RUNTIME)

    def post_message(self, message):
        response = self.boto.post_text(botName=BOT_NAME, botAlias=BOT_ALIAS, userId=str(self.user_id), inputText=message)

        if 'intentName' in response:
            intent_name = response['intentName']
            intent = Intent.enum_from_string(intent_name)

            if intent == Intent.TODAYS_SCHEDULE:
                #get schedule from google
                return Calendar.get_todays_schedule()

        if 'message' in response:
            return response['message']
