__author__ = 'martinrasumoff'

import requests
import cnfg
from pymongo import MongoClient
from requests_oauthlib import OAuth1


config = cnfg.load(".twitter_config")

oauth = OAuth1(config["consumer_key"],
               config["consumer_secret"],
               config["access_token"],
               config["access_token_secret"])

client = MongoClient("52.25.140.201",27017)

db = client['Beachbody']
coll_tweets = db['tweets']


for each in coll_tweets.find({}):
    tweet_txt = each['text']

    hashtag_list = []
    tweeter_list = []

    tweet_wrd_list = tweet_txt.split()

    for word in tweet_wrd_list:
        if word[0] == '@':
            tweeter_list.append(word)
        else:
            if word[0] == '#':
                hashtag_list.append(word)

    get_id = each['status_id']
    coll_tweets.update({"status_id" : get_id}, {"$set":{"hashtags": hashtag_list, "tweeter_list": tweeter_list}})

print 'a'
