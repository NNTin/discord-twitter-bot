import sys
import unittest


class TestPython(unittest.TestCase):
    def test_python(self):
        def get_python_version():
            return ".".join(map(str, sys.version_info[:3]))

        python_ok = (3, 7) > sys.version_info >= (3, 6, 0)

        self.assertTrue(
            python_ok,
            "discord-twitter-bot needs Python >=3.6.0, <3.7. You are using: "
            + get_python_version(),
        )
