import calendar
from os import walk, close, remove
from os.path import join

from datetime import datetime

from Entity import Entity, Types
from SemesterFactory import SemesterFactory


class ClassInstance(object):
    """Represents a particular Morea Class Instance. Parses the markdown files in the morea directory and keeps track
    of the modules, outcomes, readings, experiences, assessments, and prerequisites."""

    def __init__(self, moreaPath):
        """Parses the morea directory in moreaPath to create the Entities."""
        goodEnding = False
        if moreaPath.endswith("morea"):
            goodEnding = True
        if moreaPath.endswith("morea/"):
            goodEnding = True
        if not goodEnding:
            raise ValueError("Path does not end with morea")

        self.entities = {}
        self.startDate = None
        for dirpath, dirnames, filenames in walk(moreaPath):
            for name in filenames:
                if name.endswith('.md'):
                    id = None
                    title = None
                    type = None
                    startDate = None
                    endDate = None
                    published = False
                    with open(join(dirpath, name)) as morea_file:
                        for line in morea_file:
                            if line.startswith('published'):
                                index = line.find(':') + 2
                                end = len(line) - 1
                                if line[index:end].lower() == "true":
                                    published = True
                            if line.startswith('morea_id'):
                                index = line.find(':') + 2
                                end = len(line) - 1
                                id = line[index:end]
                            if line.startswith('title'):
                                index = line.find(':') + 2
                                end = len(line) - 1
                                title = line[index:end]
                            if line.startswith('morea_type'):
                                index = line.find(':') + 2
                                end = len(line) - 1
                                type = line[index:end]
                            if line.startswith('morea_start_date'):
                                index = line.find('"') + 1
                                end = len(line) - 2
                                datestr = line[index:end]
                                try:
                                    startDate = datetime.strptime(datestr, '%Y-%m-%d')
                                except ValueError:
                                    try:
                                        startDate = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
                                    except ValueError:
                                        startDate = datetime.strptime(datestr, "%Y-%m-%dT%H:%M")
                            if line.startswith('morea_end_date'):
                                index = line.find('"') + 1
                                end = len(line) - 2
                                datestr = line[index:end]
                                try:
                                    endDate = datetime.strptime(datestr, '%Y-%m-%d')
                                except ValueError:
                                    try:
                                        endDate = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
                                    except ValueError:
                                        endDate = datetime.strptime(datestr, "%Y-%m-%dT%H:%M")
                        #print id, title, type, startDate, endDate
                        if self.startDate == None and startDate != None:
                            self.startDate = startDate
                        elif startDate != None and startDate < self.startDate:
                            self.startDate = startDate
                        e = Entity(id, title, type, morea_file.name, startDate, endDate)
                        # print e
                        try:
                            if self.entities[type] == None:
                                self.entities[type] = []
                        except KeyError, err:
                            self.entities[type] = []
                        if published:
                            self.entities[type].append(e)
        # print self.entities
        self.readingDays = {}
        try:
            for r in self.entities[Types.reading.name]:
                day = r.getStartWeekDay()
                if day != None:
                    try:
                        self.readingDays[day] = self.readingDays[day] + 1
                    except KeyError:
                        self.readingDays[day] = 1
        except KeyError:
            print "No readings!?"
        self.experienceDays = {}
        self.homeworks = []
        try:
            for e in self.entities[Types.experience.name]:
                day = e.getStartWeekDay()
                if day != None:
                    try:
                        self.experienceDays[day] = self.experienceDays[day] + 1
                    except KeyError:
                        self.experienceDays[day] = 1
                if e.isDueFridayEvening():
                    self.homeworks.append(e)
        except KeyError:
            print "No experineces?"
        self.semesterFactory = SemesterFactory()

    def __str__(self):
        return "{0}: {1} modules | {2} outcomes | {3} readings | {4} experiences | {5} assessments ".format(self.getSemester().name,
            self.getNumModules(),
                                                                                                       self.getNumOutcomes(),
                                                                                                       self.getNumReadings(),
                                                                                                       self.getNumExperiences(),
                                                                                                       self.getNumAssessments())

    def __repr__(self):
        return self.__str__()

    def getNumModules(self):
        return len(self.entities[Types.module.name])

    def getNumOutcomes(self):
        return len(self.entities[Types.outcome.name])

    def getNumReadings(self):
        return len(self.entities[Types.reading.name])

    def getNumExperiences(self):
        return len(self.entities[Types.experience.name])

    def getNumAssessments(self):
        return len(self.entities[Types.assessment.name])

    def getNumPrerequisites(self):
        return len(self.entities[Types.prerequisite.name])

    def getMeetingDays(self):
        ret = []
        for k in self.readingDays.keys():
            ret.append(calendar.day_name[k - 1])
        return ret

    def isMW(self):
        """Returns True if this class is a Monday Wednesday class."""
        days = self.getMeetingDays()
        if len(days) == 2:
            if days[0] == "Monday" and days[1] == "Wednesday":
                return True
        elif len(days) == 3:
            if days[0] == "Monday" and days[1] == "Wednesday":
                return True
        return False

    def isTR(self):
        """Returns True if this class is a Monday Wednesday class."""
        days = self.getMeetingDays()
        if len(days) == 2 and days[0] == "Tuesday" and days[1] == "Thursday":
            return True
        return False

    def getSemester(self):
        """Returns the Semester this course is in."""
        return self.semesterFactory.getSemester(self.startDate)
