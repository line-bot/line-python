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
        print(req)
        line.push_massage(req['source']['userId'],"ちょっとまってね....")
        go_req = requests.get("https://motivating-menu.appspot.com/api/phase1")
        go_req_text = go_req.text[:-1]
        go_req_text = go_req_text[1:]
        go_req_text = go_req_text.replace("\\","")
        data = factory.to_message(json.loads(go_req_text))
        line.push_massage(req['source']['userId'],"グッとくる画像をえらんでね")
        line.reply(req['replyToken'],data)

    def to_postback(self,req):
        req_data = json.loads(req['postback']['data'])
        if req_data['state'] == '0':
            line.push_massage(req['source']['userId'],"ちょっとまってね....")
            go_req = requests.get("https://motivating-menu.appspot.com/api/phase2?category_id=" + req_data['id'])
            data = factory.to_postback(json.loads(go_req.text),req_data['id'])
            line.push_massage(req['source']['userId'],"どれにする？")
            line.reply(req['replyToken'],data)

        elif req_data['state'] == '1':
            data = factory.to_coco(req_data)
            print (req_data)
            line.push_massage(req['source']['userId'],"検索中......")
            line.reply(req['replyToken'],data)
            go_req = requests.get("https://motivating-menu.appspot.com/api/phase3?category_id=" + req_data['id'] + "&menu_id=" + req_data['menu_id'])
            print(go_req.text)

controller = Controller()
