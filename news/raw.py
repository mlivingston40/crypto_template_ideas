import requests


class News:

    def __init__(self, keywords):

        self.keywords = keywords

    #data from bing news api -- microsofts 'cognitive services'...free for now, but will cost $ at scale
    def get_news(self):

        news = []

        for k in self.keywords:

            for p in requests.get("https://api.cognitive.microsoft.com/bing/v7.0/news/search?q={}&count=10&mkt=en-us&safeSearch=Moderate&sortBy=Date".format(k),
                                  headers={'Ocp-Apim-Subscription-Key': '68d0fcdb0a944081b6d3fcc5f96ca653'}).json().items():

                if p[0] == 'value':

                    for n in p[1]:

                        news.append([n['name'], n['description'], n['url']])

        return news


