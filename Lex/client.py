import boto3
import falcon

class Messages(object):
    def on_post(self, req, resp):
        client = boto3.client('lex-runtime')
        response = client.post_text(botName='PizzaBot', botAlias='BETA', userId='abcd1234', inputText='I would like a pizza')
        print(response)
        resp.body = response['message']
        resp.status = falcon.HTTP_200
