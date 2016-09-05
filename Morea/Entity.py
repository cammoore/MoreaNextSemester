from tempfile import mkstemp
from os import close, remove
from shutil import move
from enum import Enum


class Types(Enum):
    module = 1
    outcome = 2
    reading = 3
    experience = 4
    assessment = 5
    prerequisite = 6


class Entity(object):
    """Represents a Morea Entity with an id, title, type, optional morea_start_date, morea_end_date."""

    def __init__(self, id, title, type, filePath, startDate=None, endDate=None):
        """Creates a new Entity."""
        self.id = id
        self.title = title
        if type.lower() == Types.module.name:
            self.type = Types.module.name
        if type.lower() == Types.outcome.name:
            self.type = Types.outcome.name
        if type.lower() == Types.reading.name:
            self.type = Types.reading.name
        if type.lower() == Types.experience.name:
            self.type = Types.experience.name
        if type.lower() == Types.assessment.name:
            self.type = Types.assessment.name
        if type.lower() == Types.prerequisite.name:
            self.type = Types.prerequisite.name
        self.filePath = filePath
        self.startDate = startDate
        self.endDate = endDate

    def __str__(self):
        return "MoreaEntity[id={0}, title={1}, type={2}, startDate={3}, endDate={4}]".format(self.id, self.title, self.type, self.startDate, self.endDate)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if type(other) is type(self):
            return self.id == other.id and self.title == other.title and self.type == other.type and \
                   self.startDate == other.startDate and self.endDate == other.endDate


    def hasDate(self):
        """Returns True if the entity has a startDate or endDate."""
        return self.startDate is not None or self.endDate is not None

    def getStartWeekDay(self):
        """Returns the ISO day of the week for the startDate. Monday = 1, Sunday = 7."""
        if self.startDate != None:
            return self.startDate.isoweekday()
        else:
            return self.startDate

    def getEndWeekDay(self):
        """Returns the ISO day of the week for the endDate. Monday = 1, Sunday = 7."""
        if self.endDate != None:
            return self.endDate.isoweekday()
        else:
            return self.endDate

    def isDueFridayEvening(self):
        """Returns true if the startDate is late Friday night."""
        if self.startDate != None:
            if self.startDate.isoweekday() == 5:
                if self.startDate.hour > 21:
                    return True
                else:
                    return False
        return False

    def getDurationInDays(self):
        """Returns the number of days for the entity or None if the entity doesn't have a start or end date."""
        if self.startDate != None and self.endDate != None:
            dur = self.endDate - self.startDate
            return dur.days
        return None

    def endsOnDay(self, isoDay):
        """Returns True if the entity ends on the given isoDay"""
        if self.endDate != None and self.endDate.isoweekday() == isoDay:
            return True
        return False

    def endsOnFriday(self):
        """Returns True if the entity ends on Friday."""
        if self.endDate != None:
            return self.endsOnDay(5) or self.endDate.isoweekday() == 6 and self.endDate.hour == 0 and self.endDate.minute == 0
        return False

    def startsOnDay(self, isoDay):
        """Returns True if the entity starts on the given isoDay"""
        if self.startDate != None and self.startDate.isoweekday() == isoDay:
            return True
        return False

    def startsOnFriday(self):
        """Returns True if the entity starts on Friday."""
        return self.startsOnDay(5)

    def startsOnSaturday(self):
        """Returns True if the entity starts on Saturday."""
        return self.startsOnDay(6)

    def startsMonThur(self):
        """Returns true if the entity starts Monday - Thursday"""
        if self.startDate is not None:
            if self.startDate.isoweekday() < 6:
                return True
        return False

    def isModWeekLong(self):
        """Returns True if the duration is a multiple of weeks."""
        if self.getDurationInDays() != None:
            return self.getDurationInDays() % 7 == 0
        return False

    def isWeekly(self):
        """Returns True if the duration starts on Saturday and ends on Friday"""
        return self.startsOnSaturday() and self.endsOnFriday()

    def updateFileDates(self, delta):
        """Updates the morea_start_date and morea_end_date lines in the file associated with this entity."""
        fh, abs_path = mkstemp()
        with open(abs_path,'w') as new_file:
            with open(self.filePath) as old_file:
                for line in old_file:
                    if line.startswith('morea_start_date') and self.startDate != None:
                        try:
                            new_file.write(self.__processStartDateLine(line, delta))
                        except ValueError:
                            print self.filePath, 'has an error '
                            new_file.write(line)
                    elif line.startswith('morea_end_date') and self.endDate != None:
                        try:
                            new_file.write(self.__processEndDateLine(line, delta))
                        except ValueError:
                            print self.filePath, 'has an error '
                            new_file.write(line)
                    else:
                        new_file.write(line)
        close(fh)
        # Remove original file
        remove(self.filePath)
        # Move new file
        move(abs_path, self.filePath)

    def __processStartDateLine(self, line, delta):
        """Parses the morea_start_date or morea_end_date line to create a datetime then updates the time by delta.
        Returns the updated line."""
        index = line.find('"') + 1
        d = self.startDate
        self.startDate = d + delta
        return '{0}{1}"\n'.format(line[:index],self.startDate.strftime('%Y-%m-%dT%H:%M:%S'))

    def __processEndDateLine(self, line, delta):
        """Parses the morea_start_date or morea_end_date line to create a datetime then updates the time by delta.
        Returns the updated line."""
        index = line.find('"') + 1
        d = self.endDate
        self.endDate = d + delta
        return '{0}{1}"\n'.format(line[:index],self.endDate.strftime('%Y-%m-%dT%H:%M:%S'))

