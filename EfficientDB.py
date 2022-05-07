class EfficientDB:
    def __init__(self, value=None):
        self._db = {}
        self._update_all_value = value
        self._update_all_timestamp = 0
        self._last_update = 0

    def set(self, key, value):
        self._last_update = self._update_all_timestamp + 1
        vector = [value, self._last_update]
        self._db[key] = vector

    @property
    def last_update(self):
        return self._update_all_value

    def timestamp(self, val=None):
        if val is not None:
            vector = self._db[val]
            return vector[1]
        else:
            return self._update_all_timestamp

    def value_of(self, key):
        if self._update_all_timestamp < self._db[key][1]:
            self._db[key][0] = self._update_all_value
            self._db[key][1] = self._update_all_timestamp
        return self._db[key][0]

    def set_all(self, value):
        self._update_all_value = value
        now = self._last_update
        self._update_all_timestamp = now + 1

    def isEmpty(self):
        return len(self._db) == 0

    def set_dict(self):
        for key in self._db.keys():
            if self._db[key][1] < self._update_all_timestamp:
                self._db[key][0] = self._update_all_value

    def set_and_get_dict(self):
        self.set_dict()
        return self._db
