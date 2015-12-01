import pandas as pd
from textblob import TextBlob
import sys
import matplotlib.pyplot as plt

reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_csv("/Users/martinrasumoff/Desktop/JobSearch/tweets_csv4")

polarity_list = []
subjectivity_list = []
polarity_list_bod = []
subjectivity_list_bod = []

for each in df['text']:
    texto = "u'"+each
    sent = TextBlob(texto).sentiment
    polarity = sent[0]
    subjectivity = sent[1]
    if "#BOD" in each:
        polarity_list_bod.append(polarity)
        subjectivity_list_bod.append(subjectivity)

    polarity_list.append(polarity)
    subjectivity_list.append(subjectivity)

polarity_series = pd.Series(polarity_list,name="polarity")
subjectivity_series = pd.Series(subjectivity_list,name="subjectivity")
polarity_series_bod = pd.Series(polarity_list_bod,name="polarity_bod")
subjectivity_series_bod = pd.Series(subjectivity_list_bod,name="subjectivity_bod")

frames = [df,polarity_series,subjectivity_series]
frames2 = [polarity_series_bod,subjectivity_series_bod]

df2 = pd.concat(frames,axis=1)
df2.to_csv("/Users/martinrasumoff/Desktop/JobSearch/tweets_csv_sentiment")

df3 = pd.concat(frames2,axis=1)

x1 = df2['polarity']
y1 = df2['subjectivity']
x2 = df3['polarity_bod']
y2 = df3['subjectivity_bod']


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,7))
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.xticks(rotation='vertical')

ax1.plot(x1, y1, marker='+', color='r', linestyle='None', label='Overall')
ax1.legend(['Tweet Sentiment'])
ax2.plot(x2, y2, marker='*', color='b', linestyle='None', label='#BOD')
ax2.legend(['Tweet Sentiment (#BOD Only)'])
plt.show()

df4 = df2[df2['polarity'] >=0.60]

for each in df4['text']:
    print each
    print "-----------------------"

print "Descriptive Stats"
print "-----------------"
print "Polarity Mean: "+str(df2['polarity'].mean())
print "Polarity Stdv: "+str(df2['polarity'].std())
print "-----------------"
print "Subjectivity Mean: "+str(df2['subjectivity'].mean())
print "Subjectivity Stdv: "+str(df2['subjectivity'].std())

print 'hi'

