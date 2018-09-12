import tweepy
from textblob import TextBlob

consumer_key = 'YagPZOlFWVZ0YPbdmUEzyyNku'
consumer_secret = 'Jhux6HgX6BkwClbTkGlKCw80SqzG7dRVhn7gUlf7ABAPVPGKXt'

access_token = '1039525420901621760-IipxTAmrNzPsHOjQD0EsNIkScDlKBK'
access_secret = 'n6Py1kG0LIh2N1WrOO2MK8yGjppSfqFdLlhXUoUKS9tny'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)