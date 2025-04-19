import re
import html
from clients.GameSpotClient import GameSpotClient


class GameSpotClientAdapter():
    def __init__(self):
        self.gameSpotClient: GameSpotClient = GameSpotClient()

    def getArticles(self):
        articleResponses = self.gameSpotClient.getArticles()
        if articleResponses and len(articleResponses) > 0:
            articleTags = articleResponses.find_all("article")
            return [self.buildArticleObject(str(article)) for article in articleTags]
        return []

    def buildArticleObject(self, markup: str) -> dict:
        # Define regex patterns for each field
        titlePattern = r"<title>(.*?)</title>"
        bodyPattern = r"<body>(.*?)</body>"
        authorsPattern = r"<authors>(.*?)</authors>"
        imagePattern = r"<image>(.*?)</image>"
        deckPattern = r"<deck>(.*?)</deck>"

        # Extract fields using regex
        title = re.search(titlePattern, markup, re.DOTALL)
        body = re.search(bodyPattern, markup, re.DOTALL)
        authors = re.search(authorsPattern, markup, re.DOTALL)
        image = re.search(imagePattern, markup, re.DOTALL)
        deck = re.search(deckPattern, markup, re.DOTALL)

        # Build the dictionary with extracted fields
        articleData = {
            "title": title.group(1).strip() if title else None,
            "body": self.sanitizeText(body.group(1).strip()) if body else None,
            "authors": authors.group(1).strip() if authors else None,
            "image": image.group(1).strip() if image else None,
            "deck": self.sanitizeText(deck.group(1).strip()) if deck else None,
        }

        return articleData
    
    def sanitizeText(self, text: str) -> str:
        sanitizedText = text.replace("\\'", "'").replace(r'\"', '"')
        sanitizedText = html.unescape(sanitizedText)
        sanitizedText = re.sub(r'\\[abfnrtv]', '', sanitizedText)
        sanitizedText = sanitizedText.replace('\\', '').replace('/', '')

        sanitizedText = " ".join(sanitizedText.split())
        return sanitizedText

