# -*- coding: utf-8 -*-
from api.line import line
import service.factory as factory
import requests
import json

class Controller(object):
    def middleware(self,req):
        # print(req['type'])
        if req['type'] == 'message':
            self.to_message(req)
        elif req['type'] == 'postback':
            # print (req)
            self.to_postback(req)
    def to_message(self,req):
        go_req = requests.get("https://motivating-menu.appspot.com/api/phase1")
        go_req_text = go_req.text[:-1]
        go_req_text = go_req_text[1:]
        go_req_text = go_req_text.replace("\\","")
        print (go_req_text)
        data = factory.to_message(json.loads(go_req_text))
        line.reply(req['replyToken'],data)

    def to_postback(self,req):
        req_data = json.loads(req['postback']['data'])
        if req_data['state'] == '0':
            go_req = requests.get("https://motivating-menu.appspot.com/api/phase2?category_id=" + req_data['id'])

            hogehoge=[
            {
                "id": "1",
                "name": "カレー",
                "imageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg"
              },
              {
                "id": "2",
                "name": "やきそば",
                "imageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg"
              },
              {
                "id": "3",
                "name": "めんつゆ",
                "imageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg"
              },
              {
                "id": "4",
                "name": "どんぶり",
                "imageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg"
              },
              {
                "id": "5",
                "name": "かつお",
                "imageUrl": "https://s3-us-west-2.amazonaws.com/lineapitest/hamburger_240.jpeg"
              },
            ]

            # print(go_req.text)
            # print(type(hogehoge['hoge'][0]['imageUrl']))
            print(go_req.text)
            data = factory.to_postback(json.loads(go_req.text),req_data['id'])
            # return
            # data = factory.to_postback(hogehoge,req_data['id'])

            line.reply(req['replyToken'],data)


controller = Controller()
