import tweepy

auth = tweepy.auth.OAuthHandler('oyA4zCfF5gib2gpbeFI2fRkck', '0eLW5cXg4AUocbYHyKr6K2DTwHcWIahKzqIfIiaKmbCC7hFx3A')
auth.set_access_token('912818063543869441-v2E1YzoYCSm7xTZHPbtQkJr92TNevAf', 'eI3HtXu7HRHsjOWiGAzPqLmvKMrajQnjhMVDoBFxjNbMT')

api = tweepy.API(auth)

class Tweets:
    def __init__(self, keywords):

        self.keywords = keywords

    def get_tweets(self):

        tweets = []

        for i in self.keywords:

            for tweet in api.search(
                    q=i,
                    count=10,
                    result_type="recent",
                    lang="en"):
                tweets.append([tweet.created_at, tweet.text])
        return tweets

