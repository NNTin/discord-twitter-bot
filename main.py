#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from discordWebhooks import Webhook, Attachment, Field
import calendar, time, secret, random

followedTwitterIDs = ['31403828', '761313186284920832', '748870151215443968', '4692074893', '4575793752', '4554478933', '4487728163', '3907466052', '3593639369', '3440528535', '3439668053', '3432655593', '3338968180', '3310327604', '3303269889', '3242480829', '3216123239', '3052050280', '3047038643', '3037290961', '3033487485', '2996610345', '2970958139', '2956754815', '2955166565', '2938938385', '2889270322', '2879514418', '2870796886', '2869324601', '2865716541', '2812310104', '2800406853', '2796397921', '2780646499', '2777312755', '2773714579', '2725228346', '2649708270', '2615830670', '2604251359', '2603869602', '2592744180', '2582252852', '2567400864', '2553552858', '2491371260', '2482513555', '2481913412', '2471345334', '2469779858', '2467195614', '2464043784', '2459703620', '2445701851', '2428452410', '2411955139', '2410784130', '2404681705', '2400228572', '2386217856', '2382714398', '2372553726', '2361167905', '2352066902', '2348870683', '2340148272', '2339669515', '2329911342', '2321353982', '2319965270', '2285204556', '2280441901', '2265082196', '2235742716', '2235339294', '2227724430', '2196643610', '2191768050', '2191044079', '2175366870', '2154246463', '2148067442', '1962751351', '1948009400', '1943370512', '1940262770', '1940226188', '1930032192', '1890112758', '1882748173', '1879369416', '1864753722', '1863948846', '1861889875', '1852461140', '1710754705', '1689114020', '1686409308', '1681728685', '1646385560', '1604298906', '1585064574', '1572641863', '1530999505', '1530822530', '1510291615', '1472179928', '1470288122', '1466374340', '1452520626', '1444517990', '1423590463', '1393184251', '1392357157', '1378252098', '1374715688', '1359382638', '1336663478', '1335093780', '1324698572', '1287142711', '1283594461', '1273010972', '1270683193', '1260872838', '1252989409', '1246701048', '1231238136', '1228156986', '1225892959', '1185749900', '1168302188', '1124889985', '1114208214', '1082642528', '1079659363', '1075335967', '1067825672', '1066198542', '1064941080', '1063719126', '1028324108', '1018372472', '1009146318', '1001675731', '983235152', '976425312', '974976086', '949785073', '946665630', '946385166', '938707458', '931383470', '894006060', '888340963', '866794232', '862055424', '860766001', '852129608', '845005633', '834078912', '824303286', '819130742', '807261433', '799327212', '792306224', '789731714', '778719132', '764406294', '746882864', '742437204', '738920474', '737005568', '730428108', '719299243', '714535189', '702218011', '637385264', '634640251', '627793203', '623422331', '622515222', '620034214', '617809885', '613451573', '602275012', '602096713', '595609086', '586206841', '582344429', '580265247', '580029672', '576649003', '576185800', '564965493', '564626355', '563776499', '562375245', '560659842', '554772598', '550312731', '548773222', '548654902', '548611932', '547293931', '542925461', '538267747', '521928542', '514529146', '507182348', '502879331', '500042471', '499855365', '496751891', '493159187', '492809987', '489727015', '474796055', '474739648', '461319570', '461147700', '460851542', '457503645', '451884361', '450411157', '442452107', '433788176', '432279860', '430068547', '429466096', '399070033', '393715760', '390150419', '384552831', '373059738', '372867550', '370215189', '366653082', '363923240', '357500748', '356965621', '356348186', '354584470', '352636258', '349535869', '346740028', '346729702', '328266448', '321525822', '315742624', '312937997', '312417114', '309366491', '308422941', '303814178', '302739636', '295495025', '294697122', '287564504', '287284747', '284996272', '284982697', '283906817', '281164402', '277385620', '276254547', '275003449', '266442619', '261653690', '260900027', '257268592', '256755816', '251277482', '242848378', '242266033', '238658567', '237097346', '236700415', '226438738', '224393767', '221123734', '217217185', '213921115', '211464941', '210232104', '207120515', '204857157', '194773220', '194518592', '184977478', '183241224', '175479505', '169165191', '153288720', '147605676', '143314273', '139169385', '137024504', '131242768', '108685424', '101144163', '96925846', '95164862', '92747246', '87267381', '83568017', '79551388', '75740838', '65211941', '57537292', '52082053', '49644939', '48952825', '47100679', '47051634', '45319754', '44680622', '42384354', '40644641', '36803580', '33230443', '30083335', '29506286', '29145184', '26332904', '26191204', '25143672', '23911853', '22397537', '22351672', '21648994', '20488747', '20447194', '20175678', '19976791', '19768807', '19503627', '18490175', '18227338', '17388199', '16905329', '15027884', '14427787', '13038392', '11821362', '5636712']
colors = ['#7f0000', '#535900', '#40d9ff', '#8c7399', '#d97b6c', '#f2ff40', '#8fb6bf', '#502d59', '#66504d', '#89b359', '#00aaff', '#d600e6', '#401100', '#44ff00', '#1a2b33', '#ff00aa', '#ff8c40', '#17330d', '#0066bf', '#33001b', '#b39886', '#bfffd0', '#163a59', '#8c235b', '#8c5e00', '#00733d', '#000c59', '#ffbfd9', '#4c3300', '#36d98d', '#3d3df2', '#590018', '#f2c200', '#264d40', '#c8bfff', '#f23d6d', '#d9c36c', '#2db3aa', '#b380ff', '#ff0022', '#333226', '#005c73', '#7c29a6']

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_status(self, status):
        """Called when a new status arrives"""
        try:
            data = status._json




            sendIt = False

            wh = Webhook(url=secret.WEBHOOK_URL, username="Chirp",
                         icon_url="http://cdn.dota2.com/apps/dota2/images/heroes/rattletrap_lg.png")
            if data['user']['id_str'] in followedTwitterIDs: #filter out tweets from people replying to dota 2 personalities

                text = ''
                if 'extended_tweet' in data:
                    text = data['extended_tweet']['full_text']
                else:
                    text = data['text']

                for url in data['entities']['urls']:
                    if url['expanded_url'] == None:
                        continue
                    text = text.replace(url['url'], "[%s](%s)" %(url['display_url'],url['expanded_url']))

                for userMention in data['entities']['user_mentions']:
                    text = text.replace('@%s' %userMention['screen_name'], '[@%s](http://twitter.com/%s)' %(userMention['screen_name'],userMention['screen_name']))

                media_url = ''
                if 'extended_tweet' in data:
                    for media in data['extended_tweet']['entities']['media']:
                        if media['type'] == 'photo':
                            media_url = media['media_url']

                if 'media' in data['entities']:
                    for media in data['entities']['media']:
                        if media['type'] == 'photo':
                            media_url = media['media_url']






                at = Attachment(author_name=data['user']['screen_name'],
                                author_icon=data['user']['profile_image_url'],
                                color=random.choice(colors), pretext=text,
                                image_url=media_url,
                                title_link="https://twitter.com/" + data['user']['screen_name'] + "/status/" + str(data['id_str']),
                                footer="Tweet created at",
                                footer_icon="https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697029-twitter-512.png",
                                ts=calendar.timegm(time.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y')))

                print(data['user']['screen_name'], 'says: ', text)

                wh.addAttachment(at)



                #if ('retweeted_status' in data): #not reliable. Twitter data is not consistent.
                if ('quoted_status' in data):


                    text = data['quoted_status']['text']
                    for url in data['quoted_status']['entities']['urls']:
                        if url['expanded_url'] == None:
                            continue
                        text = text.replace(url['url'], "[%s](%s)" % (url['display_url'], url['expanded_url']))

                    for userMention in data['quoted_status']['entities']['user_mentions']:
                        text = text.replace('@%s' %userMention['screen_name'], '[@%s](http://twitter.com/%s)' %(userMention['screen_name'],userMention['screen_name']))



                    field = Field(data['quoted_status']['user']['screen_name'], text)
                    at.addField(field)


                    sendIt = True




            if (sendIt or True):
                wh.post()

        except:
            print('@@@@@@@@@@@@@@@@@@@@@@')
            print(data)
            print(type(data))





        return True


    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        print('on_delete')
        print(status_id)
        print(user_id)
        return

    def on_event(self, status):
        """Called when a new event arrives"""
        print('on_event')
        print(status)
        return

    def on_direct_message(self, status):
        """Called when a new direct message arrives"""
        print('on_direct_message')
        print(status)
        return

    def on_friends(self, friends):
        """Called when a friends list arrives.
        friends is a list that contains user_id
        """
        print('on_friends')
        print(friends)
        return

    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        print('on_limit')
        print(track)
        return

    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        print('on_error')
        print(status_code)
        return False

    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice
        Disconnect codes are listed here:
        https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
        """
        print('on_disconnect')
        print(notice)
        return

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        print('on_warning')
        print(notice)
        return


if __name__ == '__main__':
    print('Starting bot....')
    l = StdOutListener()
    auth = OAuthHandler(secret.CONSUMER_KEY, secret.CONSUMER_SECRET)
    auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['soccer', 'basketball'])
    while True:
        try:
            stream.filter(follow=followedTwitterIDs)           #TODO: reenable it
            #stream.filter(track=['soccer', 'basketball'])
        except:
            time.sleep(5)
            print('restarting')