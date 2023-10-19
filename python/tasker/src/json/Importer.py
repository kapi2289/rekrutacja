import json


class Importer:
    tasks = []

    def __init__(self):
        pass

    def read_tasks(self):
        with open("taski.json") as f:
            self.tasks = json.load(f)

    def get_tasks(self):
        return self.tasks
