import json


class Dumper:

    @staticmethod
    def dump(data, file_name):
        with open(f'{file_name}.json', 'w') as fp:
            json.dump(data, fp)

