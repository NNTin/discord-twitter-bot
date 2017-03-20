#Examples using all parameters
import secret


from discordWebhooks import Webhook, Attachment, Field

url = secret.WEBHOOK_URL
#url = "https://discordapp.com/api/webhooks/293188566123544576/ZtX8XieGCmQqoFiY7haklXHhCHAFqGEv-TU06xWDby_0pCs_HD-1K130zDI_yoBT2KPu"
wh = Webhook(url, "Text content", "Username", "http://cdn.dota2.com/apps/dota2/images/heroes/rattletrap_lg.png")
#wh = Webhook(url=url, username="username", icon_url="https://www.facebook.com/favicon.ico")


at = Attachment(author_name = "Author Name", author_icon = "https://www.facebook.com/favicon.ico", color = "#ffffff",
            pretext = "pretext", title = "title (with title_link)", title_link = "http://github.com",
            image_url = "http://www.cekane.fr/wp-content/uploads/2015/10/googlelogosept12015.png",
            footer = "footer (with footer_icon)", footer_icon = "https://www.facebook.com/favicon.ico", ts="100197000")


field = Field("Field title", "Field value with Short (aligned)", True)
at.addField(field)
field = Field("Field title", "Field value with Short (aligned)", True)
at.addField(field)
field = Field("Field title", "Field value with Short (aligned)", True)
at.addField(field)
field = Field("Field title", "Field value without Short", False)
at.addField(field)
field = Field("Field title", "Field value without Short", False)
at.addField(field)

wh.addAttachment(at)

at = Attachment(author_name = "Second Attachment Author Name", color = "#0000ff", title = "Title")
wh.addAttachment(at)


wh.post()