#coding: utf-8

import json
import requests
import time

class Webhook():
    def __init__(self, url, content="", username="", icon_url=""):
        """
        Initialize a Discord Webhook object.
        @param {String} url - The webhook url where to make requests.
        @param {String} content - TODO: Document this variable usage.
        @param {String} username - The username to use while sending data to the webhook, may be left blank.
        @param {String} icon_url - An icon url, may be left blank.
        """
        self.url = url
        self.content = content
        self.username = username
        self.icon_url = icon_url
        self.formatted = ""
        self.attachments = []

    def addAttachment(self, attachment):
        """
        Add a specified Attachment to self.attachments for later usage.
        @param {Attachment} attachment - The Attachment object to append.
        """
        if isinstance(attachment, Embed):
            self.attachments.append(attachment)
        else:
            raise Exception("The attachment is not a correct attachment object")

    def format(self):
        """
        Format the current object as a valid JSON object.
        """
        data = {"username": self.username, "content": self.content, "avatar_url": self.icon_url, "embeds": []}

        for attachment in self.attachments:
            att = {"author": attachment.author, "color": attachment.color, "description": attachment.description,
                   "title": attachment.title, "url": attachment.url, "footer": attachment.footer,
                   "timestamp": attachment.timestamp, "fields": []}
            if attachment.type == "photo":
                att["image"] = attachment.image
            if attachment.type == "video":
                att["video"] = attachment.video

            for field in attachment.fields:
                f = {}
                f["name"] = field.name
                f["value"] = field.value
                f["inline"] = field.inline
                att["fields"].append(f)

            data["embeds"].append(att)

        self.formatted = json.dumps(data)

    def post(self):
        """
        Send the JSON formated object to the specified `self.url`.
        """
        self.format()
        #print(self.formatted)
        result = requests.post(self.url, data=self.formatted, headers={"Content-Type": "application/json"})

        if 200 <= result.status_code <= 299 or result.text == "ok":
            return True
        else:
            try:
                jsonResult = json.loads(result.text)
                if jsonResult['message'] == 'You are being rate limited.':
                    print(jsonResult)
                    wait = int(jsonResult['retry_after'])
                    wait = wait/1000 + 0.1
                    time.sleep(wait)
                    self.post()
                else:
                    print(str(result.text))
                    print(type(result.text))
                    print(result.text)
                    print(jsonResult)
            except:
                #raise Exception("Error on post : " + str(result))
                print('Unhandled Error! Look into this')
                print(str(result.text))
                print(type(result.text))
                print(result.text)
        #else:
        #    raise Exception("Error on post : " + str(result))

class Embed(classmethod):
    def __init__(self, **args):
        """
        Initialize an Attachment object and fill the properties from given $args.
        """
        self.author = {"name": args["author_name"] if "author_name" in args else "",
                       "url": args["author_url"] if "author_url" in args else "",
                       "icon_url": args["author_icon"] if "author_icon" in args else ""}
        self.color = args["color"] if "color" in args else ""
        self.description = args["description"] if "description" in args else ""
        self.title = args["title"] if "title" in args else ""
        self.url = args["url"] if "url" in args else ""
        if "media_type" in args:
            if args["media_type"] == "photo":
                self.image = {"url": args["media_url"]}
            if args["media_type"] == "video":
                self.video = {"url": args["media_url"]}
        self.type = args["media_type"] if "media_type" in args else ""
        self.footer = {"text": args["footer"] if "footer" in args else "",
                       "icon_url": args["footer_icon"] if "footer_icon" in args else ""}
        self.timestamp = args["timestamp"] if "timestamp" in args else 0
        self.fields = []

    def addField(self, field):
        """
        Add a field to the current Attachment object.
        @param {Fields} field - The field object to add to this attachment.
        """
        if isinstance(field, Field):
            self.fields.append(field)
        else:
            raise Exception("The field is not a correct field object")

class Field():
    def __init__(self, title="", value="", short=False):
        """
        Initialize a Field object.
        @param {String} title - The field title (aka. key).
        @param {String} value - The field value.
        @param {Boolean} short - TODO: Document usage of this variable.
        """
        self.name = title
        self.value = value
        self.inline = short