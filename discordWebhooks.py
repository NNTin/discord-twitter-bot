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
        self.url = url if "/slack" in url else url + "/slack"
        self.content = content
        self.username = username
        self.icon_url = icon_url
        self.formated = ""
        self.attachments = []

    def addAttachment(self, attachment):
        """
        Add a specified Attachment to self.attachments for later usage.
        @param {Attachment} attachment - The Attachment object to append.
        """
        if isinstance(attachment, Attachment):
            self.attachments.append(attachment)
        else:
            raise Exception("The attachment is not a correct attachment object")

    def format(self):
        """
        Format the current object as a valid JSON object.
        """
        data = {}
        data["username"] = self.username
        data["text"] = self.content
        data["icon_url"] = self.icon_url

        data["attachments"] = []
        for attachment in self.attachments:
            att = {}
            data["username"] = attachment.author_name
            data["icon_url"] = attachment.author_icon

            att["author_name"] = attachment.author_name
            att["author_icon"] = attachment.author_icon
            att["color"] = attachment.color
            att["pretext"] = attachment.pretext
            att["title"] = attachment.title
            att["title_link"] = attachment.title_link
            att["image_url"] = attachment.image_url
            att["footer"] = attachment.footer
            att["footer_icon"] = attachment.footer_icon
            att["ts"] = attachment.ts

            att["fields"] = []
            for field in attachment.fields:
                f = {}
                f["title"] = field.title
                f["value"] = field.value
                f["short"] = field.short
                att["fields"].append(f)

            data["attachments"].append(att)

        self.formated = json.dumps(data)

    def post(self):
        """
        Send the JSON formated object to the specified `self.url`.
        """
        self.format()
        result = requests.post(self.url, data=self.formated).text

        if result == "ok":
            return True
        else:
            try:
                jsonResult = json.loads(result)
                if jsonResult['message'] == 'You are being rate limited.':
                    print(jsonResult)
                    wait = int(jsonResult['retry_after'])
                    wait = wait/1000 + 0.1
                    time.sleep(wait)
                    self.post()
                else:
                    print(str(result))
                    print(type(result))
                    print(result)
                    print(jsonResult)
            except:
                #raise Exception("Error on post : " + str(result))
                print('Unhandled Error! Look into this')
                print(str(result))
                print(type(result))
                print(result)
                print(jsonResult)
        #else:
        #    raise Exception("Error on post : " + str(result))

class Attachment(classmethod):
    def __init__(self, **args):
        """
        Initialize an Attachment object and fill the properties from given $args.
        """
        self.author_name = args["author_name"] if "author_name" in args else ""
        self.author_icon = args["author_icon"] if "author_icon" in args else ""
        self.color = args["color"] if "color" in args else ""
        self.pretext = args["pretext"] if "pretext" in args else ""
        self.title = args["title"] if "title" in args else ""
        self.title_link = args["title_link"] if "title_link" in args else ""
        self.image_url = args["image_url"] if "image_url" in args else ""
        self.footer = args["footer"] if "footer" in args else ""
        self.footer_icon = args["footer_icon"] if "footer_icon" in args else ""
        self.ts = args["ts"] if "ts" in args else 0
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
        self.title = title
        self.value = value
        self.short = short