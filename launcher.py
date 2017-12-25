from dataIO import fileIO
import sys, os, subprocess, re, time
try:
    import pip
except ImportError:
    pip = None
try:
    import tweepy
except ImportError:
    tweepy = None

REQS_DIR = "lib"
sys.path.insert(0, REQS_DIR)
IS_WINDOWS = os.name == "nt"
PYTHON_OK = sys.version_info >= (3, 5)
REQS_TXT = "requirements.txt"
INTRO = ("==============================\n"
         "discord-twitter-bot - Launcher\n"
         "==============================\n")

class configuration:
    def __init__(self):
        self.data = fileIO("data.json", "load")

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.data['Twitter']['consumer_key'],
                                   self.data['Twitter']['consumer_secret'])
        auth.set_access_token(self.data['Twitter']['access_token'],
                              self.data['Twitter']['access_token_secret'])
        self.client = tweepy.API(auth)

    def getConfig(self, compact=False):
        if not compact:
            print(self.data)
        else:
            for key in self.data['Twitter']:
                print('{}: {}'.format(key, self.data['Twitter'][key]))
            self.webhookCount()

    def setTwitterCredentials(self):
        print('Setting up Twitter!\nGet your Twitter API keys & secret as well as access token & secret from here: https://apps.twitter.com/')
        for key in self.data['Twitter']:
            self.data['Twitter'][key] = cleanInput(key + ': ')
        try:
            self.authenticate()
        except:
            print('Could not find tweepy library. Did you install requirements?')
        try:
            self.client.verify_credentials()
        except:
            print('Your Twitter credentials are wrong!')
        else:
            print('Your Twitter credentials are set and correct!')
            c.saveConfig()

    def saveConfig(self):
        fileIO("data.json", "save", self.data)

    def webhookCount(self):
        amountWebhooks = len(self.data['Discord'])
        amountChannels = 0
        amountTwitterUsers = 0
        for i in range(0, amountWebhooks):
            amountChannels += len(self.data['Discord'][i]['webhook_urls'])
            amountTwitterUsers += len(self.data['Discord'][i]['twitter_ids'])

        print('You currently have {} webhooks in {} channels with a total amount of {} followed twitter users.'
              .format(amountWebhooks, amountChannels, amountTwitterUsers))

    def lookup_users_list(self, twitter_ids):
        full_users = []
        user_count = len(twitter_ids)
        while True:
            for i in range(0, int((user_count // 100)) + 1):
                full_users.extend(self.client.lookup_users(user_ids=twitter_ids[i * 100:min((i + 1) * 100, user_count)]))
            print('getting users batch: {}'.format(i))
            return full_users

    def getValidTwitterIDs(self, twitter_ids):
        validTwitterIDs = []
        try:
            self.authenticate()
            self.client.verify_credentials()
        except:
            print('Could not check Twitter IDs because Twitter API Credentials are invalid.')
            return validTwitterIDs

        user_objs = self.lookup_users_list(twitter_ids)

        for user in user_objs:
            print('twitter id: {} -> screen name: {}'.format(user.id, user.screen_name))
            validTwitterIDs.append(str(user.id))
        return validTwitterIDs

    def addWebhook(self):
        while True:
            print('Do you want to setup your Webhook via Twitter IDs or a Twitter List URL?')
            print("1. Twitter IDs")
            print("2. Twitter List URL")
            print("\n0. Quit")
            choice = user_choice()
            if choice == "1":
                self.addWebhookViaTwitterIDs()
                break
            elif choice == "2":
                self.addWebhookViaTwitterURL()
                break
            elif choice == "0":
                break

    def addWebhookViaTwitterURL(self):
        self.webhookCount()
        self.authenticate()
        print('\nYou can post the same content in multiple text channels by separating the webhook URLs with a comma ,')

        webhook_url = input('Give webhook URL: ').split(',')
        twitterListURL = input(
            'The Twitter List URL needs to be in this format: https://twitter.com/XXXXXXXX/lists/XXXXXXXXX/.\n'
            'Give me a Twitter List URL:')
        print('\nProgram is now attempting to communicate with Twitter. This can take a while!')

        twitter_ids = []
        pattern = '^https?:\/\/(?:www\.)?twitter\.com\/(?P<twittername>[a-zA-Z0-9]+)\/lists\/(?P<listname>[a-zA-Z0-9-]+)'
        for m in re.finditer(pattern, twitterListURL, re.I):

            for member in tweepy.Cursor(self.client.list_members, m.group('twittername'), m.group('listname')).items():
                twitterID = member._json['id_str']
                if twitterID not in twitter_ids:
                    twitter_ids.append(twitterID)

        self.getValidTwitterIDs(twitter_ids)
        print('Added %s Twitter users to the webhook URL' % len(twitter_ids))

        includeReplyToUser = get_bool(
            'Include reply tweets from other Twitter users? (Random Twitter user is replying to your followed Twitter user) (true/false)')
        includeUserReply = get_bool(
            'Include reply tweets to other Twitter users? (Your followed Twitter user is replying to random non-followed Twitter users.) (true/false)')
        includeRetweet = get_bool(
            'Include Retweets? (true/false)')

        self.data['Discord'].append(
            {'webhook_urls': webhook_url, 'twitter_ids': twitter_ids, 'IncludeReplyToUser': includeReplyToUser,
             "IncludeUserReply": includeUserReply, "IncludeRetweet": includeRetweet})
        c.saveConfig()


    def addWebhookViaTwitterIDs(self):
        self.webhookCount()
        print('\nYou can post the same content in multiple text channels by separating the webhook URLs with a comma ,')
        print('Get the twitter IDs from here: http://gettwitterid.com/')
        print('You can follow multiple twitter users by separating the twitter IDs with a comma ,')

        webhook_url = cleanInput('Give webhook URL: ').split(',')
        twitter_ids = str(input('Give twitter IDs: ').replace(' ', '')).split(',')
        includeReplyToUser = get_bool(
            'Include reply tweets from other Twitter users? (Random Twitter user is replying to your followed Twitter user) (true/false)')
        includeUserReply = get_bool(
            'Include reply tweets to other Twitter users? (Your followed Twitter user is replying to random Twitter users.) (true/false)')
        includeRetweet = get_bool('Include Retweets? (true/false)')

        originalCount = len(twitter_ids)
        twitter_ids = self.getValidTwitterIDs(twitter_ids)
        print('Of the {} twitter ids {} were valid.'.format(originalCount, len(twitter_ids)))

        if (len(twitter_ids) != 0):
            self.data['Discord'].append(
                {'webhook_urls': webhook_url, 'twitter_ids': twitter_ids, 'IncludeReplyToUser': includeReplyToUser,
                 "IncludeUserReply": includeUserReply, "IncludeRetweet": includeRetweet})
            c.saveConfig()
        else:
            print('Your twitter IDs were invalid. Thus the webhook was not added. A Twitter ID is made up of numbers.')

    def listWebhooks(self):
        for i in range(0, len(self.data['Discord'])):
            whString = ''
            for j in range(0, len(self.data['Discord'][i]['webhook_urls'])):
                whString += self.data['Discord'][i]['webhook_urls'][j] + ' '
            print('{}. webhook URL(s): {}'.format(i+1, whString[:-1]))
        print('\n0. Cancel')

    def removeWebhook(self):
        print('Listing all your webhooks.')
        self.listWebhooks()
        index = inputNumber('Which webhook do you want to delete?')
        if index == 0:
            print('Cancelled. Nothing was deleted')
            return
        elif index < len(self.data['Discord'])+1:
            del self.data['Discord'][index-1]
        else:
            print('This is not a valid option!')
        c.saveConfig()

def inputNumber(text):
    while True:
        try:
            return int(input(text).replace(' ', ''))
            break
        except:
            print('This is not a number!')

def cleanInput(text):
    return input(text).replace(' ', '')

def get_bool(prompt):
    while True:
        try:
           return {"true":True,"false":False}[input(prompt).lower().replace(' ','')]
        except KeyError:
           print("Invalid input please enter True or False!")

def check_files():
    f = "data.json"
    if not fileIO(f, "check"):
        print("data.json does not exist. Creating empty data.json...")
        fileIO(f, "save",
            {
                "Twitter": {
                    "consumer_key": "",
                    "consumer_secret": "",
                    "access_token": "",
                    "access_token_secret": ""
                },
                "Discord": [],
                "twitter_ids": []
            }
        )

def wait():
    input("Press enter to continue.")

def user_choice():
    return input("> ").lower().replace(' ', '')

def get_python_version():
    return ".".join(map(str, sys.version_info[:3]))

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def install_reqs():
    interpreter = sys.executable
    if interpreter is None:
        print("Python interpreter not found.")
        return
    args = [
        interpreter, "-m",
        "pip", "install",
        "--upgrade",
        "--target", REQS_DIR,
        "-r", REQS_TXT
    ]
    code = subprocess.call(args)

    if code == 0:
        print("\nRequirements setup completed.")
    else:
        print("\nAn error occurred and the requirements setup might "
              "not be completed. Consult the docs.\n")

def runBot(autorestart=False):
    interpreter = sys.executable

    if interpreter is None:  # This should never happen
        raise RuntimeError("Couldn't find Python's interpreter")

    cmd = (interpreter, "main.py")

    while True:
        try:
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            code = 0
            break
        else:
            if autorestart:
                print('Unknown crash. Sleeping for 10 minutes.')
                time.sleep(600)
            else:
                break

if __name__ == '__main__':
    if not PYTHON_OK:
        print('discord-twitter-bot needs Python 3.5 or superior. You are using: ' + get_python_version())
        wait()
        exit(1)
    if pip is None:
        print("discord-twitter-bot cannot work without the pip module. Please make sure to "
              "install Python without unchecking any option during the setup")
        wait()
        exit(1)
    if tweepy is None:
        print("Warning: tweepy is not installed. Please run the first option.\n")

    check_files()

    c = configuration()

    while True:
        print(INTRO)
        print("1. Install requirements")
        print("2. Set Twitter Credentials")
        print("3. Add a webhook")
        print("4. Remove a webhook")
        print("5. Print config")
        print("6. Start the bot")
        print("7. Start the bot with auto-rerun")
        print("\n0. Quit")
        choice = user_choice()
        if choice == "1":
            install_reqs()
            try:
                import tweepy
            except ImportError:
                print('Installing tweepy failed. Please contact me with reproduction steps.')
            wait()
        elif choice == "2":
            c.setTwitterCredentials()
            wait()
        elif choice == "3":
            c.addWebhook()
            wait()
        elif choice == "4":
            c.removeWebhook()
            wait()
        elif choice == "5":
            c.getConfig(compact=False)
            print()
            c.getConfig(compact=True)
            wait()
        elif choice == "6":
            runBot(autorestart=False)
            wait()
        elif choice == "7":
            runBot(autorestart=True)
            wait()
        elif choice == "0":
            break
        clear_screen()