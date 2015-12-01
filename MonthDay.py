
from datetime import datetime
import pandas as pd

#tweet_df = pd.read_csv("/Users/martinrasumoff/Desktop/JobSearch/tweets_csv","rb")
#tweet_df = pickle.load(open("/Users/martinrasumoff/Desktop/JobSearch/tweets_","rb"))

df = pd.read_csv("/Users/martinrasumoff/Desktop/JobSearch/tweets_csv2.csv", encoding='utf-8')

month_list = []
day_list = []

for index in range(len(df)):

    date_object = datetime.strptime(df['date_txt'][index][0:10], '%a %b %d')

    df_month = date_object.month
    df_day = date_object.day

    month_list.append(df_month)
    day_list.append(df_day)

month_series = pd.Series(month_list, name='month')
day_series = pd.Series(day_list, name='day')

frames = [df,month_series,day_series]
df = pd.concat(frames, axis=1)

df.to_csv("/Users/martinrasumoff/Desktop/JobSearch/tweets_csv4", encoding='utf-8')


print 'hi'
