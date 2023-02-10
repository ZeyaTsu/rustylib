import urllib.request
import json

class Request:
    request_url:str = None
    
    def __init__(self, url:str):
        self.request_url = url
        self.url = url

    def send(self, timeout:int=5) -> bool:
        try:
            req = urllib.request.Request(self.url)
            req.add_header("User-Agent", "Mozilla/5.0")
            response = urllib.request.urlopen(req, timeout=timeout)
            return True
        except urllib.error.HTTPError as e:
            print(f"Rusty HTTP Error : {e.code}")
            return False
        except urllib.error.URLError as e:
            print(f"Rusty Network Error : {e.reason}")
            return False
    
    def getJson(self, jsontag):
        req = urllib.request.Request(self.url)
        req.add_header("User-Agent", "Mozilla/5.0")
        try:
            response = urllib.request.urlopen(req, timeout=5)
            dataWanted = json.loads(response.read().decode())
            return dataWanted[jsontag]
        except urllib.error.HTTPError as e:
            print(f"HTTP error: {e.code}")
            return None
        except urllib.error.URLError as e:
            print(f"Network error: {e.reason}")
            return None

    def get(self, tag):
        with urllib.request.urlopen(self.url) as res:
            if self.send() == True:
                dataWanted = json.loads(res.read().decode())
                return dataWanted[tag]