import json
import os
from random import randint

class InvalidFileIO(Exception):
    pass

class DataIO():
    #def __init__(self):

    def save_json(self, filename, data):
        """Atomically saves json file"""
        rnd = randint(1000, 9999)
        path, ext = os.path.splitext(filename)
        tmp_file = "{}-{}.tmp".format(path, rnd)
        self._save_json(tmp_file, data)
        try:
            self._read_json(tmp_file)
        except json.decoder.JSONDecodeError:
            return False
        os.replace(tmp_file, filename)
        return True

    def load_json(self, filename):
        """Loads json file"""
        return self._read_json(filename)

    def is_valid_json(self, filename):
        """Verifies if json file exists / is readable"""
        try:
            self._read_json(filename)
            return True
        except FileNotFoundError:
            return False
        except json.decoder.JSONDecodeError:
            return False

    def _read_json(self, filename):
        with open(filename, encoding='utf-8', mode="r") as f:
            data = json.load(f)
        return data

    def _save_json(self, filename, data):
        with open(filename, encoding='utf-8', mode="w") as f:
            json.dump(data, f, indent=4,sort_keys=True,
                separators=(',',' : '))
        return data

    def _legacy_fileio(self, filename, IO, data=None):
        """Old fileIO provided for backwards compatibility"""
        if IO == "save" and data != None:
            return self.save_json(filename, data)
        elif IO == "load" and data == None:
            return self.load_json(filename)
        elif IO == "check" and data == None:
            return self.is_valid_json(filename)
        else:
            raise InvalidFileIO("FileIO was called with invalid"
                " parameters")

def get_value(filename, key):
    with open(filename, encoding='utf-8', mode="r") as f:
        data = json.load(f)
    return data[key]

def set_value(filename, key, value):
    data = fileIO(filename, "load")
    data[key] = value
    fileIO(filename, "save", data)
    return True

dataIO = DataIO()
fileIO = dataIO._legacy_fileio # backwards compatibility
