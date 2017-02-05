# -*- coding: utf-8 -*-
import requests
import json
from util.settings import settings

_REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
_PUSH_ENDPOINT = 'https://api.line.me/v2/bot/message/push'

class Line(object):
    def __init__(self):
        conf = settings.get_line_conf()
        self.secret = conf['Secret']
        self.token = conf['Token']
        self.header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + self.token
    }
    def reply(self,token,data):
        data['replyToken'] = token
        req = requests.post(_REPLY_ENDPOINT, headers=self.header, data=json.dumps(data))
        print(req.text)
    def push(self,to,data):
        data['to'] = to
        req = requests.post(_PUSH_ENDPOINT, headers=self.header, data=json.dumps(data))
    def push_massage(self,to,text):
        data = {
            "messages":[
                {
                    "type":"text",
                    "text":text
                }
            ]
        }
        self.push(to,data)
line = Line()
