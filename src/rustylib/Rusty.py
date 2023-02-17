import requests
import json
import time
from .Rrequests import Request


class Rusty:
    def wait():
        while True:
            input("")
            break

    def fori(var:int, function):
        if var == 0:
            var += 1
        for i in range(var):
            function()

    def mkStrJoin(LIST_NAME, splitCaracter=''):
        FINAL_STR_JOIN_RETURN = ""
        for i, string, in enumerate(LIST_NAME):
            if i == 0:
                FINAL_STR_JOIN_RETURN += string
            else:
                FINAL_STR_JOIN_RETURN += splitCaracter + string
        return FINAL_STR_JOIN_RETURN

    def mkStr(LIST_NAME, splitCaracter='') -> str:
        LIST_NAME = str(LIST_NAME)
        LIST_NAME = LIST_NAME.replace("[","").replace("]","").replace(",",splitCaracter).replace("'","")
        return LIST_NAME
    
    def ord(c):
        if len(c) !=1:
            raise TypeError('Rusty Error - 1 Character is expected.')
        return ord(c.encode('utf-8')[0])
    
    def hashCode(string:str):
        hash = 0
        for c in string:
            hash = (31 * hash + ord(c)) & 0xFFFFFFFF
        return ((hash + 0x80000000) & 0xFFFFFFFF) - 0x80000000

    def strioReverse(string:str) -> str:
        cache = []
        reversed_str = []
        for letters in string:
            cache.append(letters)
        valueLEN = len(string)
        for i in range(len(string)):
            reversed_str.append(cache[valueLEN-1])
            valueLEN -= 1 
        return Rusty.mkStrJoin(reversed_str)

    def pkginfo():
        NAME = 'rustylib'
        VERSION = '1.8.1'
        cache = []
        web = Request("https://raw.githubusercontent.com/ZeyaTsu/rustylib/main/Rpkg_info.json")
        res = web.send()
        if res == True:
            cache.append(NAME)
            cache.append(web.get("name"))
            cache.append(VERSION)
            cache.append(web.get("version"))
            if cache[0] != cache[1]:
                print(f"Error - name: {NAME} doesn't match with {cache[1]}")
            if cache[2] != cache[3]:
                print(f"Error - version: {VERSION} doesn't match with {cache[3]}")

            print(f"     You | Correct info")
            print("_________|_____________")
            print(f"{NAME} | {cache[1]}")
            print(f"{VERSION}    | {cache[3]}")
        cache.clear()
    
    def clear(LIST_NAME, exception=None):
        if exception is not None:
            STORE = exception
        for i in range(len(LIST_NAME) - 1, -1, -1):
            LIST_NAME.pop(i)
        if exception is not None:
            LIST_NAME.insert(0, STORE)
        return LIST_NAME              
"""
Webhook
"""

class Webhook:
    webhook_url:str = None
    trying_to_connect = 0

    def __init__(self, url:str):
        self.webhook_url = url
        self.url = url
        self.embed = {}
        self.embed["fields"] = []
        
    def setTitle(self,title:str):
        self.embed["title"] = title
        
    def setDesc(self,description:str):
        self.embed["description"] = description
    
    def addField(self,name:str,value:str):
        self.embed["fields"].append({"name": name, "value": value})
        
    def sendEmbed(self):
        data = {
            "embeds": [self.embed]
        }
        requests.post(self.url, json=data)

    def sendMsg(self, message:str):
        data = {"content": message}
        headers = { "Content-Type": "application/json" }
        requests.post(self.webhook_url, data=json.dumps(data), headers=headers)

    def getResult(self):
        web = Request(self.webhook_url)
        res = web.send()
        if res == True:
            return True
        else:
            return False

    def connectToAgent(self, statut=False):
        try:
            if self.getResult() == True:
                print("Perfeclty connected to Webhook:")
                print(self.webhook_url)
                print("!help for help.")
                while True:
                    user_msg = str(input("Message > "))
                    if user_msg.startswith("!connect:"):
                        user_msg = user_msg.replace("!connect:", "")
                        if user_msg == "":
                            print("Error: Webhook doesn't exist.")
                            time.sleep(2)
                            break
                        self.webhook_url = user_msg
                        self.connectToAgent()
                    elif user_msg == "!q:t":
                        print("Disconnected")
                        self.sendMsg("Disconnected")
                        break
                    elif user_msg == "!q":
                        print("Disconnected")
                        break
                    elif user_msg == "!help":
                        print("!q:t - Quit and send the message 'Disconnected'")
                        print("!q - Quit without sending any message")
                        print("!embed - Make an embed")
                        print("!connect:new_webhook_link - Connect to another discord webhook")
                        print("______________________________________________________________________")
                    elif user_msg == "!embed":
                        title = str(input("Title: "))
                        description = str(input("Description: "))
                        field = str(input("Field: "))
                        value = str(input("Value: "))
                        self.setTitle(title)
                        self.setDesc(description)
                        self.addField(field, value)
                        print(f"Confirm: {title}\n {description}\n\n{field}\n {value}\n y/n")
                        confirm = str(input(": "))
                        if confirm.lower() == "y":
                            self.sendEmbed()
                    else:
                        self.sendMsg(user_msg)
            else:
                self.trying_to_connect += 1 
                print(f"\nTrying to connect... {self.trying_to_connect}")
                if self.trying_to_connect >= 8:
                    print("Rusty Error - Cannot reach webhook")
                    print("Press Enter to leave...")
                    Rusty.wait()
                else:
                    time.sleep(2)
                    self.connectToAgent()

        except (EOFError, KeyboardInterrupt):
            if statut == True:
                print("Connection was lost")
            print("Closing program.")
            time.sleep(1)
    
    def getInfo(self, info=None):
        web = Request(self.webhook_url)
        res = web.send()
        if res == True:
            if info == None:
                type = web.getJson("type")
                idw = web.getJson("id")
                name = web.getJson("name")
                avatar = web.getJson("avatar")
                channel_id = web.getJson("channel_id")
                guild_id = web.getJson("guild_id")
                app_id = web.getJson("application_id")
                token = web.getJson("token")

                content = [
                    "type:", type,
                    "id:", idw,
                    "name:", name,
                    "avatar:", avatar,
                    "channel ID:", channel_id,
                    "guild ID:", guild_id,
                    "application ID:", app_id,
                    "token:", token,
                ]
                return content

            elif info == "type":
                return web.getJson("type")
            elif info == "id":
                return web.getJson("id")
            elif info == "name":
                return web.getJson("name")
            elif info == "avatar":
                return web.getJson("avatar")
            elif info == "channel_id":
                return web.getJson("channel_id")
            elif info == "guild_id":
                return web.getJson("guild_id")
            elif info == "app_id":
                return web.getJson("application_id")
            elif info == "token":
                return web.getJson("token")
        else:
            print("Rusty Error: Webhook doesn't exist")          

"""

Will use rustylib.request when it'll be done :p

"""

class Rplus:
    def __init__(self):
        self.data = {}
    
    def keepThis(self, name, values):
        self.data[name] = values
    
    def removeThis(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Rusty Error - No such name in data")

    def getThis(self, name):
        return self.data.get(name)

import re

class Rconsole:
    """
    pattern for variables : 
        name:type = value
    """
    def __init__(self):
        start_str = "RUSTY - CONSOLE v:beta"
        print(start_str)
        self.variables = {}
        while True:
            prompt = str(input("rusty-cmd >>> "))
            
            passing = self.check(prompt)
            if passing != True:
                pass

            pattern = re.compile(r"^(\w+):(\w+)\s*=\s*(\w+)$")
            match = pattern.search(prompt)

            if match:
                var_name = match.group(1)
                var_type = match.group(2)
                var_value = match.group(3)
                self.variables[var_name] = (var_type, var_value)
                print(f"{var_name} ({var_type}) = {var_value}")
            else:
                try:
                    wait = eval(prompt)
                    if wait is None:
                        pass
                    else:
                        print(wait)
                except:
                    try:
                        local_namespace = {}
                        for var_name, (var_type, var_value) in self.variables.items():
                            local_namespace[var_name] = eval(f"{var_type}({var_value})")
                        print(eval(prompt, {}, local_namespace))
                    except Exception as e:
                        print(prompt)

    def check(self, prompt):
        if prompt == "webhook":
            url = str(input("URL>>> "))
            web = Webhook(url)
            print("'help' to get help.")
            prompt = str(input("webhook>>> "))
            if prompt == "connect":
                try:
                    web.connectToAgent()
                except Exception as e:
                    print(e)
                    x = str(input(""))
            elif prompt == "help":
                print(f"connect - connect to the webhook ({url})")
            else:
                return False
            