__author__ = 'martinrasumoff'

import pickle
import pandas as pd

tweet_df = pickle.load(open("/Users/martinrasumoff/Desktop/JobSearch/tweets_df","rb"))

usr_city_list = []
usr_state_list = []

for each in tweet_df['user_location']:
    location = each.split(",")
    usr_city = location[0]
    try:
        usr_state = location[1]
    except IndexError:
        usr_state = ""

    usr_city_list.append(usr_city)
    usr_state_list.append(usr_state)

usr_city_serie = pd.Series(usr_city_list,name="city")
usr_state_serie = pd.Series(usr_state_list,name="state")

frames = [tweet_df,usr_city_serie,usr_state_serie]
df = pd.concat(frames, axis=1)

df.to_csv("/Users/martinrasumoff/Desktop/JobSearch/tweets_csv", encoding='utf-8')

print 'hi!'