import falcon
import requests
from keys import WATSON_CREDENTIALS
import json

WORKSPACES_URL = 'https://gateway.watsonplatform.net/conversation/api/v1/workspaces/'
MESSAGE_PATH = '/message'
API_VERSION = '2017-04-21'

class Message(object):
    def __init__(self):
        #get workspace id for office assistant
        version = {'version': API_VERSION}
        response = requests.get(WORKSPACES_URL, auth=(WATSON_CREDENTIALS['username'], WATSON_CREDENTIALS['password']), params=version)
        json = response.json()
        workspaces = json['workspaces']
        office_workspace = [d for d in workspaces if d['name'] == 'Office Assistant'][0]
        self.workspace_id = office_workspace['workspace_id']
        self.context = None

    def on_post(self, req, resp):
        #watson
        message_url = WORKSPACES_URL + self.workspace_id + MESSAGE_PATH
        #make a request to watson
        headers = {'Content-Type': 'application/json'}
        params = {'version': API_VERSION}
        #send user input and context if any
        data = {}
        #decode byte string
        text = req.stream.read().decode('utf-8')
        if text is not None:
            data['input'] = {'text': text}
        if self.context is not None:
            data['context'] = self.context
        response = requests.post(message_url, auth=(WATSON_CREDENTIALS['username'], WATSON_CREDENTIALS['password']), params=params, headers=headers, data=json.dumps(data))
        json_response = response.json()
        if 'output' in json_response:
            #send back output
            output = json_response['output']['text'][0]
            resp.body = response.text

        if 'context' in json_response:
            #keep context for next message
            self.context = json_response['context']

        resp.status = falcon.HTTP_200
