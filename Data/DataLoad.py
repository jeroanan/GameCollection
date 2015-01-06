import json


class DataLoad(object):

    def __init__(self, file_name, root_element):
        with open(file_name) as f:
            data = json.load(f)
            self.data = data[root_element]
