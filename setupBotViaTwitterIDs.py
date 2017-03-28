import json

data = {'Twitter': {}, 'Discord': []}
print('Setting up Twitter!')
data['Twitter']['consumer_key'] = input('Give Consumer Key: ')
data['Twitter']['consumer_secret'] = input('Give Consumer Secret: ')
data['Twitter']['access_token'] = input('Give Access Token: ')
data['Twitter']['access_token_secret'] = input('Give Access Token Secret: ')

print('---\n\nSetting up Discord!')
amount = int(input('How many twitterlists do you want to track? '))

print('---\n\nYou can post the same content in multiple text channels by separating the webhook URLs with a comma ,')
print('Get the twitter IDs from here: http://gettwitterid.com/')
print('You can follow multiple twitter users by separating the twitter IDs with a comma ,')

for i in range(amount):
    webhook_url = input('Give webhook URL: ').split(',')
    twitter_ids = input('Give twitter IDs: ').split(',')
    data['Discord'].append({'webhook_urls': webhook_url, 'twitter_ids': twitter_ids})
    print('---')

data['twitter_ids'] = []

for element in data['Discord']:
    data['twitter_ids'].extend(x for x in element['twitter_ids'] if x not in data['twitter_ids'])

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
