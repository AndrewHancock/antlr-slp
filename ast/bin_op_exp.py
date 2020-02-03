class BinOpExp:
    def __init__(self, left, op, right):
        self._left = left
        self._op = op
        self._right = right

    @property
    def left(self):
        return self._left

    @property
    def op(self):
        return self._op

    @property
    def right(self):
        return self._right
