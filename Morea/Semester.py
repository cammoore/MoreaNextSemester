
class Semester(object):
    """Represents an academic semester."""

    def __init__(self, name, firstDay, holidays, lastDay, startOfFinals, endOfFinals, springBreak=None):
        """Creates a new Semester instance."""
        self.name = name
        self.firstDay = firstDay
        self.lastDay = lastDay
        self.holidays = holidays
        self.startOfFinals = startOfFinals
        self.endOfFinals = endOfFinals
        self.springBreak = springBreak


    def __str__(self):
            return "Semester[Name={0}, firstDay={1}, lastDay={2}, holidays={3}, startOfFinals={4}, endOfFinals={5}, springBreak={6}]".format(self.name, self.firstDay, self.lastDay, self.holidays, self.startOfFinals, self.endOfFinals, self.springBreak)

    def __repr__(self):
        return self.__str__()
