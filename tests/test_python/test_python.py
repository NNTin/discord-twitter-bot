import sys
import unittest


class TestPython(unittest.TestCase):
    def test_python(self):
        def get_python_version():
            return ".".join(map(str, sys.version_info[:3]))

        python_ok = sys.version_info >= (3, 5, 3)

        self.assertTrue(python_ok,
                        'discord-twitter-bot needs Python 3.5.3 or superior. You are using: ' + get_python_version())
