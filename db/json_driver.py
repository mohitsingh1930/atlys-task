import json
import os

class JsonDriver:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.data = json.load(f)

    def _save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def get(self, id):
        return self.data.get(id)

    def set(self, id, value):
        self.data[id] = value
        self._save()

    def delete(self, id):
        if self.data[id]:
            del self.data[id]
            self._save()
