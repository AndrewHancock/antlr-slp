class CompoundStm():
    def __init__(self, stm1, stm2):
        self._stm1 = stm1
        self._stm2 = stm2

    @property
    def stm1(self):
        return self._stm1

    @property
    def stm2(self):
        return self._stm2
