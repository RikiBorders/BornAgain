import re
from clients.GameSpotClient import GameSpotClient


class GameSpotClientAdapter():
    def __init__(self):
        self.gameSpotClient: GameSpotClient = GameSpotClient()

    def getArticles(self):
        articles = self.gameSpotClient.getArticles()
        if articles:
            articleTags = articles.find_all("article")
            return [self.extractArticlefields(str(article)) for article in articleTags]
        return []

    def extractArticlefields(self, markup: str) -> dict:
        # Define regex patterns for each field
        titlePattern = r"<title><!\[CDATA\[(.*?)\]\]></title>"
        bodyPattern = r"<body>(.*?)</body>"
        authorsPattern = r"<authors><!\[CDATA\[(.*?)\]\]></authors>"
        imagePattern = r"<image>(.*?)</image>"
        deckPattern = r"<deck><!\[CDATA\[(.*?)\]\]></deck>"

        # Extract fields using regex
        title = re.search(titlePattern, markup, re.DOTALL)
        body = re.search(bodyPattern, markup, re.DOTALL)
        authors = re.search(authorsPattern, markup, re.DOTALL)
        image = re.search(imagePattern, markup, re.DOTALL)
        deck = re.search(deckPattern, markup, re.DOTALL)

        # Build the dictionary with extracted fields
        articleData = {
            "title": title.group(1).strip() if title else None,
            "body": body.group(1).strip() if body else None,
            "authors": authors.group(1).strip() if authors else None,
            "image": image.group(1).strip() if image else None,
            "deck": deck.group(1).strip() if deck else None,
        }

        return articleData

