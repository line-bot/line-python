# -*- coding: utf-8 -*-
import json
import requests
from flask import Flask,request
from api.line import line
from service.controller import 

req = requests.get("https://motivating-menu.appspot.com/api/phase1")

app = Flask(__name__)
@app.route("/callback", methods=['POST'])

def callback():
    print(request.json['events'][0]['replyToken'])
    # print(type(request.json['events']))

    data = {
        'messages':[
            {
                'type':'text',
                'text':'おやすみ'
            }
        ]
    }
    line.reply(request.json['events'][0]['replyToken'],data)
    return ''

if __name__ == "__main__":
   app.run(host = '0.0.0.0', port = 9000, threaded = True, debug = True)