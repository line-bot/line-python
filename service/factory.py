# -*- coding: utf-8 -*-
import json
import random

def to_coco(data):
    return {
        "messages":[
            {
    "altText": "this is a buttons template",
    "template": {
            "actions": [
                {
                    "label": "クックパッドで見る",
                    "type": "uri",
                    "uri": "https://cookpad.com/search/" + data['name']
                },
                {
                    "label": "楽天レシピで見る",
                    "type": "uri",
                    "uri": "http://recipe.rakuten.co.jp/search/" + data['name']
                },
                {
                    "label": "Nadiaで見る",
                    "type": "uri",
                    "uri": "https://oceans-nadia.com/category?q=" + data['name']
                }
            ],
            "text": data['name'],
            "thumbnailImageUrl": data['imageUrl'],
            "type": "buttons"
        },
        "type": "template"
    }
        ]
    }
def to_postback(data ,id):
    random.shuffle(data)
    data0 = json.dumps({"state":"1","menu_id":data[0]['id'],"id":id,"imageUrl":data[0]['imageUrl'], "name":data[0]['name'] })
    data1 = json.dumps({"state":"1","menu_id":data[1]['id'],"id":id,"imageUrl":data[1]['imageUrl'], "name":data[1]['name'] })
    data2 = json.dumps({"state":"1","menu_id":data[2]['id'],"id":id,"imageUrl":data[2]['imageUrl'], "name":data[2]['name'] })
    data3 = json.dumps({"state":"1","menu_id":data[3]['id'],"id":id,"imageUrl":data[3]['imageUrl'], "name":data[3]['name'] })
    data4 = json.dumps({"state":"1","menu_id":data[4]['id'],"id":id,"imageUrl":data[4]['imageUrl'], "name":data[4]['name'] })
    return {
        "messages":[
        {
            "type": "template",
            "altText": "おすすめレストラン",
            "template": {
            "type": "carousel",
            "columns": [
            {
            "thumbnailImageUrl": data[0]['imageUrl'],
            "text":data[0]['name'],
            "actions": [
            {
            "type": "postback",
            "label": "これにする",
            "data": data0
            },
            ]
            },
            {
            "thumbnailImageUrl": data[1]['imageUrl'],
            "text":data[1]['name'],
            "actions": [
            {
            "type": "postback",
            "label": "これにする",
            "data": data1
            }
            ]
            },
            {
            "thumbnailImageUrl": data[2]['imageUrl'],
            "text":data[2]['name'],
            "actions": [
            {
            "type": "postback",
            "label": "これにする",
            "data": data2
            }
            ]
            },
            {
            "thumbnailImageUrl": data[3]['imageUrl'],
            "text":data[3]['name'],
            "actions": [
            {
            "type": "postback",
            "label": "これにする",
            "data": data3
            }
            ]
            },
            {
            "thumbnailImageUrl": data[4]['imageUrl'],
            "text":data[4]['name'],
            "actions": [
            {
            "type": "postback",
            "label": "これにする",
            "data": data4
            }
            ]
            },
            ]
            }
            }
            ]
        }
def to_message(data):
    return {
    "messages":[
    {
        "type": "template",
        "altText": "おすすめレストラン",
        "template": {
        "type": "carousel",
        "columns": [
        {
        "thumbnailImageUrl": data[0]['imageUrl'],
        "text": "                           ===========================",
        "actions": [
        {
        "type": "postback",
        "label": "これにする",
        "data": '{"state":"0","id":"' + data[0]['category'] +'"}'
        },
        ]
        },
        {
        "thumbnailImageUrl": data[1]['imageUrl'],
        "text": "                           ===========================",
        "actions": [
        {
        "type": "postback",
        "label": "これにする",
        "data": '{"state":"0","id":"' + data[1]['category'] +'"}'
        }
        ]
        },
        {
        "thumbnailImageUrl": data[2]['imageUrl'],
        "text": "                           ===========================",
        "actions": [
        {
        "type": "postback",
        "label": "これにする",
        "data": '{"state":"0","id":"' + data[2]['category'] +'"}'
        }
        ]
        },
        ]
        }
        }
        ]
    }
