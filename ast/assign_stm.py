class AssignStm:
    def __init__(self, the_id, exp):
        self._id = the_id
        self._expression = exp

    @property
    def id(self):
        return self._id

    @property
    def exp(self):
        return self._expression
