class _Result(object):
    def __init__(self, reason="", details=""):
        self.reason = reason
        self.details = details

    @property
    def type(self):
        return type(self)

    @property
    def name(self):
        return type(self).__name__.upper()


class Pass(_Result):
    pass


class Skip(_Result):
    pass


class Fail(_Result):
    pass


class Error(_Result):
    pass
