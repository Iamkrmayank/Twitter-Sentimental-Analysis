# Twitter-Sentimental-Analysis

Nowadays, people from all around the world use social media to share their views or any information. 
Twitter is an online news and social networking site where people communicate in short messages called tweets. 
Users share their daily lives, post their opinions on everything such as brands and places.
Companies can benefit from this massive platform in various ways: 
• They can use twitter to increase their brand awareness 
• Inform customers about the updates 
• To get instant feedback about their product and services 
• Collect data related to opinions on them The most important thing for a company is to listen to market and meet the customers need.
When companies grow it becomes difficult for them to pay attention to each customer’s review and know what people think about them, this is where SENTIMENTAL ANALYSIS comes to use.
About the project
Twitter sentiment analysis identifies negative, positive, or neutral emotions within the text of a tweet.
It is a text analysis using natural language processing (NLP) and machine learning.


Twitter Developer API has been used as Datasets.

* In order to fetch tweets through Twitter API, one needs to create a “TWITTER DEVELOPER ACCOUNT” from twitter developer portal and register an app through their twitter account.
* Once the app is created, open the ‘Keys and Tokens’ tab, and copy ‘API Key’, ‘API Secret’, ‘Access token’ and ‘Access Token Secret’.
I carried out the following steps for the project:

Import libraries
* Tweets mining
* Data cleaning
* Tweets processing
* Data exploration
* Sentimental Analysis



<img width="420" alt="Screenshot 2023-05-09 at 5 35 01 PM" src="https://github.com/Iamkrmayank/Twitter-Sentimental-Analysis/assets/103871423/c926cdf6-bad3-43cb-957f-6a791a1d73aa">


IMPORTING LIBRARIES

Python libraries like :-

Tweepy :- for tweets mining
Pandas :- for data cleaning/manipulation
TextBlob :- for sentimental analysis
MatPlotlib :- Data exploration
WordCloud :- Data exploration
Re :- Regular expression, it lets you check is a particular string matches a given expression


Authorize twitter API client.

We use this code to fetch tweets, and filter the retweets and links after authorization of Twitter API.

<img width="642" alt="Screenshot 2023-05-09 at 5 45 52 PM" src="https://github.com/Iamkrmayank/Twitter-Sentimental-Analysis/assets/103871423/32f3db72-a23e-451f-a086-028ab30b2e99">

I created a dataframe using pandas library.

DATA CLEANING AND TWEETS PROCESSING

Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. 
The ultimate goal is to clean up the individual tweets.
To remove the mentions, #, and emojis, I created a function cleanTxt(text) which uses re library.

To make the cleaning more efficient, I converted all the tweets to lower case, removed the punctuation marks, or any irrelevant character and also removed stop words from the tokens, by using stop words library. Stop words are the commonly used words which are irrelevant in text analysis like I, am, you, are, etc. Additionally, I used a concept known as “Lemmatization”. This is a process of returning words to their “base” form. I implemented it using WordNetLemmatizer.

Note that, the more you clean your data, the more effective and accurate your result will be.

DATA EXPLORATION

WORD CLOUD

It is a visual representation of text data, which is often used to depict keyword metadata.

<img width="543" alt="Screenshot 2023-05-09 at 5 51 07 PM" src="https://github.com/Iamkrmayank/Twitter-Sentimental-Analysis/assets/103871423/3e2cce66-fb7b-4940-b327-c7c69e434bb5">

Using the WordCloud library, you can generate a Word Cloud based on the word frequency and superimpose these words on any image. In this case, I used a rectangular block and Matplotlib to display the image. The Word Cloud shows, words with higher frequency in bigger text size while “not-so” common words are in smaller text sizes. It can also be used to check whether our cleaning was successful or not, by taking a look at word cloud and seeing if the words make any sense or not.

SENTIMENTAL ANALYSIS

For this analysis, I went with TextBlob. Text Blob analyzes sentences by giving each tweet a Subjectivity and polarity score. Based on the Polarity score, one can define which tweets were Positive, Negative, or Neutral. Polarity simply means emotions expressed in a sentence. 
Emotions are closely related to sentiments. The strength of a sentiment is typically linked to the intensity of certain emotions, e.g., joy and anger. Subjectivity, subjective sentence expresses some personal feelings, views, or beliefs. 
A subjective sentence may not express any sentiment. I created two columns of subjectivity and polarity in my dataframe.

<img width="705" alt="Screenshot 2023-05-09 at 5 52 52 PM" src="https://github.com/Iamkrmayank/Twitter-Sentimental-Analysis/assets/103871423/3bfc683d-dbd6-476d-be71-9c949102d3fb">

A polarity score of < 0 is Negative, 0 is Neutral while>0 is Positive. I used the “apply” method on the “Polarity” column in my dataframe to return the respective sentiment category.
And create a column “Analysis”.
Now, subsequently analysis has been for all the positive/negative tweets or not.

POLARITY AND SUBJECTIVITY GRAPH

<img width="538" alt="Screenshot 2023-05-09 at 5 54 36 PM" src="https://github.com/Iamkrmayank/Twitter-Sentimental-Analysis/assets/103871423/5f6c9df3-3ab2-433b-af9c-fa3c70d8d55d">

Conclusion

I learned many new techniques and enjoyed the process. 
There were a lot of problems, but removing errors, yeah, that’s what we have to learn.
The project may not give accurate results in some cases as mentioned above, and there are quite a few solutions too, I will definitely explore this domain further.
