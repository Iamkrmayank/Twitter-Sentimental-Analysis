#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy  # to gather tweeter data
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
plt.style.use('fivethirtyeight')

# Twitter API Credentials
APIkey = "3OMBrpi6hg5kvQ3Zb1LMFwaEQ"
APISecretKey = "f9fEg3dmaEtqaoZW90MqvElUBV7LvKHOg2zbOPDpmPBvD8BYFt"
accessToken = "1529864260473409545-9wzTxuhcOAc5xwvtpeHYw51NpsQby3"
accessTokenSecret = "ffiOk1LMVMggUkFvMQKTVtroqQOMhJVfGc1605Iv23Tqy"
# create the object for authentication
Auth = tweepy.OAuthHandler(APIkey, APISecretKey)
Auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(Auth)
# display
posts = api.user_timeline(
    screen_name='Trump', count=100, tweet_mode='extended')
i = 1
# print(posts)
for tweet in posts[:10]:  # just want to see the top 10 from 100
    print(str(i) + ') ' + tweet.full_text + '\n')
    i = i+1

# Creating dataframe with a column having name "tweets"
df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweet'])
print(df)

# make a function to clean tweets


def cleanTxt(texts):
    texts = re.sub('@[A-Za-z0-9]+', '', texts)  # removing mentions
    texts = re.sub("#", '', texts)  # removing 
    texts = re.sub('RT[\s]+', '', texts)  # removing Retweets
    texts = re.sub('https?:\/\/\S+', '', texts)  # removing links
    return texts


df['Tweet'] = df['Tweet'].apply(cleanTxt)
print(df)
# sentiments
analysis = TextBlob("Yesterday was a brilliant day")
analysis.sentiment
# creating function to get the tweet subjectivity


def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# creating function to get the tweet Polarity


def get_polarity(text):
    return TextBlob(text).sentiment.polarity


# create 2 columns 'Subjectivity' and 'Polarity'
df['Subjectivity'] = df['Tweet'].apply(get_subjectivity)
df['Polarity'] = df['Tweet'].apply(get_polarity)
print(df)

# Lets do Analysis

# Word Cloud Visualization
allwords = ' '.join([i for i in df['Tweet']])
Cloud = WordCloud(width=500, height=300, random_state=0,
                  max_font_size=100).generate(allwords)

plt.imshow(Cloud)
plt.show()

# Creating function to process positive,neutral and negative


def getAnalysis(ranking):
    if ranking < 0:
        return 'Negative'
    elif ranking == 0:
        return 'Neutral'
    else:
        return 'Positive'


df['Analysis'] = df['Polarity'].apply(getAnalysis)
print(df)

df[df['Analysis'] == 'Neutral']

df['Analysis'].value_counts()


print(df.shape)

# plotting scatter plotgit
plt.figure(figsize=(8, 6))
for i in range(0, df.shape[0]):
    plt.scatter(df['Polarity'][i], df['Subjectivity'][i], color='Blue')

plt.title("Sentimental Analyze")
plt.xlim(-1, 1)
plt.xlabel('Polarity(x axis)')
plt.ylabel('Subjectivity(y axis)')
plt.show()
# Only 3 neutral tweets would be shown because of data overlap

df['Analysis'].value_counts().plot(kind='bar')
plt.title("Sentimental Analyze")
plt.xlabel('Polarity(x axis)')
plt.ylabel('Count(y axis)')
plt.show()

# Lets get positive tweets only
i = 1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for j in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][j] == 'Positive'):
        print(str(i) + ') ' + sortedDF['Tweet'][j])
        print()
        i = i+1

# Lets get negative tweets only
i = 1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for j in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][j] == 'Negative'):
        print(str(i) + ') ' + sortedDF['Tweet'][j])
        print()
        i = i+1


# Lets get neutral tweets only
i = 1
sortedDF = df.sort_values(by=['Polarity'], ascending=False)
for j in range(0, sortedDF.shape[0]):
    if (sortedDF['Analysis'][j] == 'Neutral'):
        print(str(i) + ') ' + sortedDF['Tweet'][j])
        print()
        i = i+1


# In[ ]:




