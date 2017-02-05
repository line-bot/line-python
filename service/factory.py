# -*- coding: utf-8 -*-
import json

def to_postback(data ,id):
    print(type(data[3]['id']))
    print(data[3]['id'])
    data0 = json.dumps({"state":"2","menu_id":data[0]['id'],"id":id})
    data1 = json.dumps({"state":"2","menu_id":data[1]['id'],"id":id})
    data2 = json.dumps({"state":"2","menu_id":data[2]['id'],"id":id})
    data3 = json.dumps({"state":"2","menu_id":data[3]['id'],"id":id})
    data4 = json.dumps({"state":"2","menu_id":data[4]['id'],"id":id})
    print(type(data0))
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
            "data": data0
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
            "data": data1
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
            "data": data2
            }
            ]
            },
            {
            "thumbnailImageUrl": data[3]['imageUrl'],
            "text": "                           ===========================",
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
            "text": "                           ===========================",
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
    # return {
    #     "messages"[
    #         {
    #             "type": "template",
    #             "altText": "おすすめレストラン",
    #             "template": {
    #                 "type": "carousel",
    #                 "columns": [
    #                     {
    #                         "thumbnailImageUrl": data[0]['imageUrl'],
    #                         "text": data[0]['name'],
    #                         "actions": [
    #                             {
    #                                 "type": "postback",
    #                                 "label": "これにする",
    #                                 "data": data0
    #                             }
    #                         ]
    #                     },
    #                 ]
    #             }
    #         }
    #     ]
    # }
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
