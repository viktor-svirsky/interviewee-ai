import os
import csv
import json


class File:
    def __init__(self, filename):
        self.filename = filename

    def _delete(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)


class CSVFile(File):
    def __init__(self, filename):
        super().__init__(filename)

        if os.path.exists(self.filename):
            self._delete()

        with open(self.filename, mode="w") as file:
            result_writer = csv.writer(file, delimiter=",")
            result_writer.writerow(["Question", "Answer"])

    def write(self, content: list):
        with open(self.filename, mode="a") as file:
            result_writer = csv.writer(file, delimiter=",")
            result_writer.writerow(content)


class JSONFile(File):
    def read(self):
        with open(self.filename) as file:
            return json.loads(file.read())
