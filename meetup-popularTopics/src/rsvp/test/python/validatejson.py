# -*- coding: utf-8 -*-

'''
Created on Jun 76, 2019

@author: ravi
'''
import json

#json_string =  '{"first_name": "Anurag", "last_name":"Rana", "key3": {"key1":"key2"}}'
json_string =  ['{"venue"::{"venue_name":"Cafe Vitus","lon":121.54731,"lat":25.052959,"venue_id":19712922},"visibility":"public","response":"no","guests":0,"member":{"member_id":221379606,"photo":"http:\/\/photos2.meetupstatic.com\/photos\/member\/8\/3\/c\/4\/thumb_263973732.jpeg","member_name":"Benita  Syu"},"rsvp_id":1658877353,"mtime":1489925471668,"event":{"event_name":"New Place! Every Saturday night multilingual caf�","event_id":"hvkmsmywfbhc","time":1490439600000,"event_url":"https:\/\/www.meetup.com\/polyglottw\/events\/238185973\/"},"group":{"group_topics":[{"urlkey":"language","topic_name":"Language & Culture"},{"urlkey":"language-exchange","topic_name":"Language Exchange"},{"urlkey":"chinese-language","topic_name":"Chinese Language"}],"group_city":"Taipei","group_country":"tw","group_id":18743595,"group_name":"Multilingual Cafe Language Exchange","group_lon":121.45,"group_urlname":"polyglottw","group_lat":25.02}}',
                '{"venue":{"venue_name":"Cafe Vitus","lon":121.54731,"lat":25.052959,"venue_id":19712922},"visibility":"public","response":"no","guests":0,"member":{"member_id":221379606,"photo":"http:\/\/photos2.meetupstatic.com\/photos\/member\/8\/3\/c\/4\/thumb_263973732.jpeg","member_name":"Benita  Syu"},"rsvp_id":1658877353,"mtime":1489925471668,"event":{"event_name":"New Place! Every Saturday night multilingual caf�","event_id":"hvkmsmywfbhc","time":1490439600000,"event_url":"https:\/\/www.meetup.com\/polyglottw\/events\/238185973\/"},"group":{"group_topics":[{"urlkey":"language","topic_name":"Language & Culture"},{"urlkey":"language-exchange","topic_name":"Language Exchange"},{"urlkey":"chinese-language","topic_name":"Chinese Language"}],"group_city":"Taipei","group_country":"tw","group_id":18743595,"group_name":"Multilingual Cafe Language Exchange","group_lon":121.45,"group_urlname":"polyglottw","group_lat":25.02}}',
                '{"venue":{"venue_name":"Cafe Vitus","lon":121.54731,"lat":25.052959,"venue_id":19712922},"visibility":"public","response":"no","guests":0,"member":{"member_id":221379606,"photo":"http:\/\/photos2.meetupstatic.com\/photos\/member\/8\/3\/c\/4\/thumb_263973732.jpeg","member_name":"Benita  Syu"},"rsvp_id":1658877353,"mtime":1489925471668,"event":{"event_name":"New Place! Every Saturday night multilingual caf�","event_id":"hvkmsmywfbhc","time":1490439600000,"event_url":"https:\/\/www.meetup.com\/polyglottw\/events\/238185973\/"},"group":{"group_topics":[{"urlkey":"language","topic_name":"Language & Culture"},{"urlkey":"language-exchange","topic_name":"Language Exchange"},{"urlkey":"chinese-language","topic_name":"Chinese Language"}],"group_city":"Taipei","group_country":"tw","group_id":18743595,"group_name":"Multilingual Cafe Language Exchange","group_lon":121.45,"group_urlname":"polyglottw","group_lat":25.02}}']

for x in json_string:
    try:
        json.loads(x.decode('utf-8'))
        print("valid json")
    except ValueError as e:
        pass
            

