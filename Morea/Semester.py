
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

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __cmp__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def isInSemester(self, d):
        """Returns True if d is in this semester."""
        if d is not None:
            return self.firstDay <= d and d <= self.endOfFinals
        return False

    def hasBreak(self):
        """Returns True if the semester has a springBreak."""
        return self.springBreak != None

    def getWeek(self, d):
        """Returns the week in the semester for the given day."""
        if self.isInSemester(d):
            if self.springBreak != None:
                if d >= self.springBreak[0] and d <= self.springBreak[1]:
                    return None
                elif d < self.springBreak[0]:
                    return (d - self.firstDay).days / 7 + 1
                elif d > self.springBreak[1]:
                    return (d - self.firstDay).days / 7
            else:
                return (d - self.firstDay).days / 7 + 1

        else:
            return None

    def getShortName(self):
        """Returns the short name for the semester."""
        return self.name[:1].lower() + self.name[len(self.name) - 2:]

