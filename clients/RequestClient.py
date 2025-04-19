from urllib.request import urlopen, Request
import sys
import os
from bs4 import BeautifulSoup

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Constants import REQUEST_HEADERS

class RequestClient():

    def __init__(self):
        pass

    def sendRequest(self, requestUrl: str):
        #  let's just return html by default for now
        try:
            return self.extractContentFromHtml(Request(requestUrl, headers=REQUEST_HEADERS))
        except Exception as e:
            print(f"Exception encountered when sending request: {requestUrl}. Exception: {e}")
            return str(e)
        
    def extractContentFromHtml(self, htmlObject):
        return BeautifulSoup(urlopen(htmlObject), features="xml")

requestClient = RequestClient()