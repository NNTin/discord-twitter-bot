from tweepy import OAuthHandler
from dotenv import load_dotenv
import yaml
import os
import re


class CustomFormatter():
    FALSE_STRINGS = ["false", "False", "f", "F", "0", "", "n", "N", "no", "No", "NO", "FALSE"]

    def to_bool(self, value: str) -> bool:
        return False if value in self.FALSE_STRINGS else True

    def format(self, value):
        return self.convert_field(*value.split("!"))

    def convert_field(self, value, conversion: str):
        if isinstance(value, str):
            if conversion == 's':        # string is alrdy a string
                return value
            elif conversion == 'b':      # turn string into a bool()
                return self.to_bool(value)
            elif conversion == 'l':      # turn string into a list()
                return value.split(',')
            elif conversion == 'll':     # turn string into a double list()
                return [v.split('+') for v in value.split(',')]
            else:
                raise ValueError("Unknown conversion specifier {0!s}".format(conversion))
        else:
            return None


CONFIG_YAML = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.yml"))
DOTENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))

load_dotenv(dotenv_path=DOTENV_PATH)
config = dict()

path_matcher = re.compile(r'\$\{([^}^{]+)\}')


def path_constructor(loader, node):
    value = node.value
    match = path_matcher.match(value)
    env_var = match.group()[2:-1]
    return os.environ.get(env_var, None)  # + value[match.end():]

yaml.add_implicit_resolver('!path', path_matcher)
yaml.add_constructor('!path', path_constructor)

with open(CONFIG_YAML, 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


config['Discord'] = [{k: v for k, v in instance.items() if v is not None} for instance in config['Discord']]


auth = OAuthHandler(config["Twitter"]["consumer_key"], config["Twitter"]["consumer_secret"])
auth.set_access_token(config["Twitter"]["access_token"], config["Twitter"]["access_token_secret"])

if __name__ == '__main__':
    print(config)
    print(os.environ.get("CONSUMER_KEY", None))