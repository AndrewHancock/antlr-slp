class EseqExp:
    def __init__(self, stm, exp):
        self._stm = stm
        self._exp = exp

    @property
    def stm(self):
        return self._stm

    @property
    def exp(self):
        return self._exp
