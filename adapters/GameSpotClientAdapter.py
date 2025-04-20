import re
import html
from clients.GameSpotClient import GameSpotClient
from Models.Article import Article
# from Modules.T5Module import T5Module 


class GameSpotClientAdapter():
    def __init__(self):
        self.gameSpotClient: GameSpotClient = GameSpotClient()
        # self.T5Module: T5Module = T5Module()

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
        return Article(
            title = title.group(1).strip() if title else None,
            body =  self.summarizeBodyForEmbed(self.sanitizeText(body.group(1).strip())) if body else None,
            authors = authors.group(1).strip() if authors else None,
            image = image.group(1).strip() if image else None,
            deck = self.sanitizeText(deck.group(1).strip()) if deck else None,
        )
    
    def sanitizeText(self, text: str) -> str:
        sanitizedText = text.replace("\\'", "'").replace(r'\"', '"')
        sanitizedText = html.unescape(sanitizedText)
        sanitizedText = re.sub(r'\\[abfnrtv]', '', sanitizedText)
        sanitizedText = re.sub(r'</?p>', '', sanitizedText, flags=re.IGNORECASE)
        sanitizedText = sanitizedText.replace('\\', '').replace('/', '')

        sanitizedText = " ".join(sanitizedText.split())
        return sanitizedText
    
    def summarizeBodyForEmbed(self, body: str) -> str:
        #TODO: use the t5 module to summarize the body.
        # return self.T5Module.summarize(body, 100, 4000, True)
        return body[:1000] + "..." if len(body) > 1000 else body
