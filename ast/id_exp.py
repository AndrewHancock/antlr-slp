class IdExp:
    def __init__(self, id_str):
        self._id = id_str

    @property
    def id(self):
        return self._id