import json, tweepy, re

data = {'Twitter': {}, 'Discord': []}
print('Setting up Twitter!')

data['Twitter']['consumer_key'] = input('Give Consumer Key: ')
data['Twitter']['consumer_secret'] = input('Give Consumer Secret: ')
data['Twitter']['access_token'] = input('Give Access Token: ')
data['Twitter']['access_token_secret'] = input('Give Access Token Secret: ')

auth = tweepy.OAuthHandler(data['Twitter']['consumer_key'], data['Twitter']['consumer_secret'])
auth.set_access_token(data['Twitter']['access_token'], data['Twitter']['access_token_secret'])

api = tweepy.API(auth)

print('---\n\nSetting up Discord!')
amount = int(input('How many twitterlists do you want to track? '))

print('---\n\nYou can post the same content in multiple text channels by separating the webhook URLs with a comma ,')

print('The program will crash if your Twitter credentials were wrong.')

for i in range(amount):
    webhook_url = input('Give webhook URL: ').split(',')

    twitterListURL = input(
        'The Twitter List URL needs to be in this format: https://twitter.com/XXXXXXXX/lists/XXXXXXXXX/.\n'
        'Give me a Twitter List URL:')

    twitter_ids = []
    pattern = 'twitter.[A-Za-z]+\/(?P<twittername>[A-Za-z]+)\/lists\/(?P<listname>[A-Za-z-0-9_]+)'
    for m in re.finditer(pattern, twitterListURL, re.I):

        for member in tweepy.Cursor(api.list_members, m.group('twittername'), m.group('listname')).items():
            twitterID = member._json['id_str']
            if twitterID not in twitter_ids:
                twitter_ids.append(twitterID)

    print('Added %s Twitter users to the webhook URL' % len(twitter_ids))

    data['Discord'].append({'webhook_urls': webhook_url, 'twitter_ids': twitter_ids})
    print('---')

data['twitter_ids'] = []

for element in data['Discord']:
    data['twitter_ids'].extend(x for x in element['twitter_ids'] if x not in data['twitter_ids'])

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
