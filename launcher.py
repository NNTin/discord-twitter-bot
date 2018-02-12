from dataIO import fileIO
import sys
import os
import subprocess
import re
import time
try:
    import pip
except ImportError:
    pip = None
try:
    import tweepy
except ImportError:
    tweepy = None
try:
    import discord
except ImportError:
    discord = None

REQS_DIR = "lib"
sys.path.insert(0, REQS_DIR)
IS_WINDOWS = os.name == "nt"
PYTHON_OK = sys.version_info >= (3, 5)
REQS_TXT = "requirements.txt"
INTRO = ("==============================\n"
         "discord-twitter-bot - Launcher\n"
         "==============================\n")


class Configuration:
    def __init__(self):
        self.data = fileIO("data.json", "load")

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.data['Twitter']['consumer_key'],
                                   self.data['Twitter']['consumer_secret'])
        auth.set_access_token(self.data['Twitter']['access_token'],
                              self.data['Twitter']['access_token_secret'])
        self.client = tweepy.API(auth)

    def run_test(self):
        print('discord-twitter-bot needs Python 3.5 or superior. You are using: ' + get_python_version())
        if PYTHON_OK:
            print('Requirement is met.')
        else:
            print('Requirement is not met.')

        if discord is None:
            print("Warning: discord is not installed. Please run the first option.\n")
            return
        else:
            if discord.version_info.major < 1:
                print(
                    "Warning: You are using the async version of discord.py ({}). This rewrite branch requires you to "
                    "install the rewrite version of discord.py.".format(discord.__version__))
            else:
                print('Discord.py ({}) is installed.'.format(discord.__version__))

        try:
            self.authenticate()
        except:
            print('Error. Tweepy might not be installed.')
            return
        else:
            print('Tweepy is installed.')
        try:
            self.client.verify_credentials()
        except:
            print('Your Twitter credentials are wrong!')
            return
        else:
            print('Your Twitter credentials are set and correct!')

        self.webhook_count()
        self.get_config(compact=False)
        self.get_config(compact=True)

        print('Checking Twitter IDs. This may take a while.')

        twitter_ids = []
        for element in self.data['Discord']:
            twitter_ids.extend(x for x in element['twitter_ids'] if x not in twitter_ids)

        original_count = len(twitter_ids)
        twitter_ids = self.get_valid_twitter_ids(twitter_ids)
        print('Of the {} twitter ids {} were valid.'.format(original_count, len(twitter_ids)))

    def get_config(self, compact=False):
        if not compact:
            print(self.data)
        else:
            for key in self.data['Twitter']:
                print('{}: {}'.format(key, self.data['Twitter'][key]))
            self.webhook_count()

    def set_twitter_credentials(self):
        print('Setting up Twitter!\nGet your Twitter API keys & secret as well as access token & secret from here: https://apps.twitter.com/')
        for key in self.data['Twitter']:
            self.data['Twitter'][key] = clean_input(key + ': ')
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
            c.save_config()

    def save_config(self):
        fileIO("data.json", "save", self.data)

    def webhook_count(self):
        amount_webhooks = len(self.data['Discord'])
        amount_channels = 0
        amount_twitter_users = 0
        for i in range(0, amount_webhooks):
            amount_channels += len(self.data['Discord'][i]['webhook_urls'])
            amount_twitter_users += len(self.data['Discord'][i]['twitter_ids'])

        print('You currently have {} webhooks in {} channels with a total amount of {} followed twitter users.'
              .format(amount_webhooks, amount_channels, amount_twitter_users))

    def lookup_users_list(self, twitter_ids):
        full_users = []
        user_count = len(twitter_ids)
        while True:
            for i in range(0, int((user_count // 100)) + 1):
                try:
                    full_users.extend(self.client.lookup_users(user_ids=twitter_ids[i * 100:min((i + 1) * 100, user_count)]))
                except:
                    print('None of your Twitter IDs are valid.')
            return full_users

    def get_valid_twitter_ids(self, twitter_ids):
        valid_twitter_ids = []
        try:
            self.authenticate()
            self.client.verify_credentials()
        except:
            print('Could not check Twitter IDs because Twitter API Credentials are invalid.')
            return valid_twitter_ids

        user_objs = self.lookup_users_list(twitter_ids)

        for user in user_objs:
            print('twitter id: {} -> screen name: {}'.format(user.id, user.screen_name))
            valid_twitter_ids.append(str(user.id))
        return valid_twitter_ids

    def add_webhook(self):
        while True:
            print('Do you want to setup your Webhook via Twitter IDs or a Twitter List URL?')
            print("1. Twitter IDs")
            print("2. Twitter List URL")
            print("\n0. Go back")
            choice = user_choice()
            if choice == "1":
                self.add_webhook_via_twitter_ids()
            elif choice == "2":
                self.add_webhook_via_twitter_url()
            elif choice == "0":
                print('Going back...')
                break
            else:
                print('\nThis is not a valid option!\n')

    def add_webhook_via_twitter_url(self):
        self.webhook_count()
        self.authenticate()
        print('\nYou can post the same content in multiple text channels by separating the webhook URLs with a comma ,')

        webhook_url = input('Give webhook URL: ').split(',')
        twitter_list_url = input(
            'The Twitter List URL needs to be in this format: https://twitter.com/XXXXXXXX/lists/XXXXXXXXX/.\n'
            'Give me Twitter List URL(s):')
        print('\nProgram is now attempting to communicate with Twitter. This can take a while!')

        twitter_ids = []
        pattern = 'https?:\/\/(?:www\.)?twitter\.com\/(?P<twittername>[a-zA-Z0-9]+)\/lists\/(?P<listname>[a-zA-Z0-9-]+)'
        for m in re.finditer(pattern, twitter_list_url, re.I):

            for member in tweepy.Cursor(self.client.list_members, m.group('twittername'), m.group('listname')).items():
                twitter_id = member._json['id_str']
                if twitter_id not in twitter_ids:
                    twitter_ids.append(twitter_id)

        self.get_valid_twitter_ids(twitter_ids)
        print('Added %s Twitter users to the webhook URL' % len(twitter_ids))

        include_reply_to_user = get_bool(
            'Include reply tweets from other Twitter users? (Random Twitter user is replying to your followed Twitter user) (true/false)')
        include_user_reply = get_bool(
            'Include reply tweets to other Twitter users? (Your followed Twitter user is replying to random non-followed Twitter users.) (true/false)')
        include_retweet = get_bool(
            'Include Retweets? (true/false)')

        self.data['Discord'].append(
            {'webhook_urls': webhook_url, 'twitter_ids': twitter_ids, 'IncludeReplyToUser': include_reply_to_user,
             "IncludeUserReply": include_user_reply, "IncludeRetweet": include_retweet})
        c.save_config()

    def add_webhook_via_twitter_ids(self):
        self.webhook_count()
        print('\nYou can post the same content in multiple text channels by separating the webhook URLs with a comma ,')
        print('Get the twitter IDs from here: http://gettwitterid.com/')
        print('You can follow multiple twitter users by separating the twitter IDs with a comma ,')

        webhook_url = clean_input('Give webhook URL: ').split(',')
        twitter_ids = str(input('Give twitter IDs: ').replace(' ', '')).split(',')
        include_reply_to_user = get_bool(
            'Include reply tweets from other Twitter users? (Random Twitter user is replying to your followed Twitter user) (true/false)')
        include_user_reply = get_bool(
            'Include reply tweets to other Twitter users? (Your followed Twitter user is replying to random Twitter users.) (true/false)')
        include_retweet = get_bool('Include Retweets? (true/false)')

        original_count = len(twitter_ids)
        twitter_ids = self.get_valid_twitter_ids(twitter_ids)
        print('Of the {} twitter ids {} were valid.'.format(original_count, len(twitter_ids)))

        if len(twitter_ids) != 0:
            self.data['Discord'].append(
                {'webhook_urls': webhook_url, 'twitter_ids': twitter_ids, 'IncludeReplyToUser': include_reply_to_user,
                 "IncludeUserReply": include_user_reply, "IncludeRetweet": include_retweet})
            c.save_config()
        else:
            print('Your twitter IDs were invalid. Thus the webhook was not added. A Twitter ID is made up of numbers.')

    def list_webhooks(self):
        for i in range(0, len(self.data['Discord'])):
            wh_string = ''
            for j in range(0, len(self.data['Discord'][i]['webhook_urls'])):
                wh_string += self.data['Discord'][i]['webhook_urls'][j] + ' '
            print('{}. webhook URL(s): {}'.format(i+1, wh_string[:-1]))
        print('\n0. Cancel')

    def modify_webhook(self):
        print('Listing all your webhooks.')
        self.list_webhooks()
        index = input_number('Which webhook do you want to modify?')
        if index == 0:
            print('Going back...')
            return
        elif index < len(self.data['Discord']) + 1:
            index -= 1
            while True:
                print('What do you want to modify?')
                print('1. Webhook URL')
                print('2. Twitter IDs')
                print('3. Filter')
                print('\n0. Go back.')
                choice = user_choice()
                if choice == "1":
                    self.data['Discord'][index]['webhook_urls'] = clean_input('Give webhook URL: ').split(',')
                elif choice == "2":
                    while True:
                        print('Do you want to add or delete Twitter IDs?')
                        print('1. Add Twitter IDs')
                        print('2. Delete Twitter IDs')
                        print('\n0. Go back.')
                        choice = user_choice()
                        if choice == "1":
                            twitter_ids = str(input('Give twitter IDs: ').replace(' ', '')).split(',')
                            original_count = len(twitter_ids)
                            twitter_ids = self.get_valid_twitter_ids(twitter_ids)
                            print('\nOf the {} twitter ids {} were valid.\n'.format(original_count, len(twitter_ids)))
                            for twitter_id in twitter_ids:
                                self.data['Discord'][index]['twitter_ids'] += [twitter_id] if twitter_id not in self.data['Discord'][index]['twitter_ids'] else []
                        elif choice == "2":
                            twitter_ids = str(input('Give twitter IDs: ').replace(' ', '')).split(',')
                            for twitter_id in twitter_ids:
                                try:
                                    self.data['Discord'][index]['twitter_ids'].remove(twitter_id)
                                except ValueError:
                                    print("\n{} couldn't be removed since the it wasn't in the list.\n".format(twitter_id))
                        elif choice == "0":
                            break

                elif choice == "3":
                    self.data['Discord'][index]['IncludeReplyToUser'] = get_bool(
                        'Include reply tweets from other Twitter users? (Random Twitter user is replying to your followed Twitter user) (true/false)')
                    self.data['Discord'][index]['IncludeUserReply'] = get_bool(
                        'Include reply tweets to other Twitter users? (Your followed Twitter user is replying to random Twitter users.) (true/false)')
                    self.data['Discord'][index]['IncludeRetweet'] = get_bool('Include Retweets? (true/false)')
                elif choice == "0":
                    break
            c.save_config()


        else:
            print('This is not a valid option!')
        c.save_config()

    def remove_webhook(self):
        while True:
            print('Listing all your webhooks.')
            self.list_webhooks()
            index = input_number('Which webhook do you want to delete?')
            if index == 0:
                print('Going back...')
                break
            elif index < len(self.data['Discord'])+1:
                del self.data['Discord'][index-1]
            else:
                print('\nThis is not a valid option!\n')
            c.save_config()


def input_number(text):
    while True:
        try:
            return int(input(text).replace(' ', ''))
            break
        except:
            print('This is not a number!')


def clean_input(text):
    return input(text).replace(' ', '')


def get_bool(prompt):
    while True:
        try:
            return {"true": True, "false": False}[input(prompt).lower().replace(' ', '')]
        except KeyError:
            print("Invalid input please enter True or False!")


def check_files():
    f = "data.json"
    if not fileIO(f, "check"):
        print("data.json does not exist. Creating empty data.json...")
        fileIO(f, "save", {
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
        # "--target", REQS_DIR,  #This has been causing problems for some users. Although I don't know what exactly is wrong with it.
        "-r", REQS_TXT
    ]
    code = subprocess.call(args)

    if code == 0:
        print("\nRequirements setup completed.")
    else:
        print("\nAn error occurred and the requirements setup might "
              "not be completed. Consult the docs.\n")


def run_bot(auto_restart=False):
    interpreter = sys.executable

    if interpreter is None:  # This should never happen
        raise RuntimeError("Couldn't find Python's interpreter")

    if tweepy is None:
        print("Warning: tweepy is not installed. Please run the first option.\n")
        wait()
        return

    if discord is None:
        print("Warning: discord is not installed. Please run the first option.\n")
        wait()
        return
    else:
        if discord.version_info.major < 1:
            print("Warning: You are using the async version of discord.py ({}). This rewrite branch requires you to "
                  "install the rewrite version of discord.py.".format(discord.__version__))

    cmd = (interpreter, "main.py")

    while True:
        try:
            print('Starting main.py. You can get back to the launcher via ctrl+c.')
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            code = 0
            break
        else:
            if auto_restart:
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

    check_files()

    c = Configuration()

    while True:
        if tweepy is None:
            print("Warning: tweepy is not installed. Please run the first option.\n")

        if discord is None:
            print("Warning: discord is not installed. Please run the first option.\n")
        else:
            if discord.version_info.major < 1:
                print("Warning: You are using the async version of discord.py ({}). This rewrite branch requires you "
                      "to install the rewrite version of discord.py. Running the first option will install the rewrite"
                      "version but your other projects may fail since they require the async version."
                      .format(discord.__version__))

        print(INTRO)
        print("1. Install requirements")
        print("2. Set Twitter Credentials")
        print("3. Add a webhook")
        print("4. Modify a webhook")
        print("5. Remove a webhook")
        print("6. Print config")
        print("7. Start the bot")
        print("8. Start the bot with auto-rerun")
        print("9. Run a test (troubleshooting)")
        print("\n0. Quit")
        choice = user_choice()
        if choice == "1":
            install_reqs()
            try:
                import tweepy
            except ImportError:
                print('Installing tweepy failed. Please contact me with reproduction steps.')
            try:
                import discord
            except ImportError:
                print('Installing discord.py rewrite version failed. Please contact me with reproduction steps.')
            wait()
        elif choice == "2":
            c.set_twitter_credentials()
            wait()
        elif choice == "3":
            c.add_webhook()
            wait()
        elif choice == "4":
            c.modify_webhook()
            wait()
        elif choice == "5":
            c.remove_webhook()
            wait()
        elif choice == "6":
            c.get_config(compact=False)
            print()
            c.get_config(compact=True)
            wait()
        elif choice == "7":
            run_bot(auto_restart=False)
            wait()
        elif choice == "8":
            run_bot(auto_restart=True)
            wait()
        elif choice == "9":
            c.run_test()
            wait()
        elif choice == "0":
            break
        clear_screen()