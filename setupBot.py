import configparser

config = configparser.RawConfigParser()

config.add_section('Twitter')
config.add_section('Discord')
config.add_section('TwitterUsers')

print('Setting up Twitter!')
config.set('Twitter', 'CONSUMER_KEY', input('Give Consumer Key: '))
config.set('Twitter', 'CONSUMER_SECRET', input('Give Consumer Secret: '))
config.set('Twitter', 'ACCESS_TOKEN', input('Give Access Token: '))
config.set('Twitter', 'ACCESS_TOKEN_SECRET', input('Give Access Token Secret: '))

print('Setting up Discord!')
config.set('Discord', 'WEBHOOK_URL', input('Give Webhook URL: '))

print('Setting up followed Twitter Users')
config.set('TwitterUsers', 'followedTwitterIDs', input('Give me the twitter IDs(!). Separate multiple Twitter IDs via commata, do not use spaces: '))


# Writing our configuration file to 'example.cfg'
with open('test.ini', 'w') as configfile:
    config.write(configfile)

