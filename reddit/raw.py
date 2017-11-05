import requests


class Comments:

    def __init__(self, keywords):

        self.keywords = keywords

    # data from reddit, last 10 comments/body for each keyword
    def get_comments(self):

        comments = []

        for k in self.keywords:

            for p in requests.get("https://api.pushshift.io/reddit/search?q={}&limit=10".format(k)).json().values():

                for c in p:

                    comments.append([c['body'], c['subreddit']])

        return comments
