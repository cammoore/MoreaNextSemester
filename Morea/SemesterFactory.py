import json

from datetime import datetime, timedelta
from Semester import Semester


class SemesterFactory(object):

    def __init__(self, filePath=None):
        """Create a new instance"""
        if filePath is None:
            filePath = "./uh-semesters.json"
        self.filePath = filePath
        self.semesters = {}
        for s in self.buildSemesters(self.filePath):
            self.semesters[self.shortName(s.name)] = s

    def shortName(self, semesterName):
        """Returns the short name for the semester s|fYY."""
        return semesterName[:1].lower() + semesterName[len(semesterName) - 2:]

    def getSemesterFromName(self, shortName):
        return self.semesters[shortName]

    def buildSemesters(self, filePath):
        """Builds an array of Semesters from the given path."""
        ret = []
        with open(filePath) as json_data:
            semesters = json.load(json_data)
            for s in semesters:
                name = s["name"]
                datestr = s["firstDay"]
                try:
                    firstDay = datetime.strptime(datestr, '%Y-%m-%d')
                except ValueError:
                    try:
                        firstDay = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
                    except ValueError:
                        firstDay = datetime.strptime(datestr, "%Y-%m-%dT%H:%M")
                datestr = s["lastDay"]
                try:
                    lastDay = datetime.strptime(datestr, '%Y-%m-%d')
                except ValueError:
                    try:
                        lastDay = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
                    except ValueError:
                        lastDay = datetime.strptime(datestr, "%Y-%m-%dT%H:%M")
                datestr = s["startOfFinals"]
                try:
                    startOfFinals = datetime.strptime(datestr, '%Y-%m-%d')
                except ValueError:
                    try:
                        startOfFinals = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
                    except ValueError:
                        startOfFinals = datetime.strptime(datestr, "%Y-%m-%dT%H:%M")
                datestr = s["endOfFinals"]
                try:
                    endOfFinals = datetime.strptime(datestr, '%Y-%m-%d')
                except ValueError:
                    try:
                        endOfFinals = datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%S')
                    except ValueError:
                        endOfFinals = datetime.strptime(datestr, "%Y-%m-%dT%H:%M")

                holidays = []
                for h in s["holidays"]:
                    holidays.append(datetime.strptime(h, '%Y-%m-%d'))
                springBreak = None
                try:
                    springBreak = s["springBreak"]
                    sb = []
                    for d in springBreak:
                        sb.append(datetime.strptime(d, "%Y-%m-%d"))
                    springBreak = sb
                except KeyError:
                    springBreak = None
                ret.append(Semester(name, firstDay, holidays, lastDay, startOfFinals, endOfFinals, springBreak))

            return ret

    def getDelta(self, s1, s2, week):
        """Returns the timedelta for semester 1 to semester 2 and the given week."""
        if s1.hasBreak():
            if s2.hasBreak():
                return s2.firstDay - s1.firstDay
            elif week < s1.getWeek(s1.springBreak[0] + timedelta(days=7)):
                return s2.firstDay - s1.firstDay
            else:
                return s2.firstDay - s1.firstDay - timedelta(days=7)
        else:
            if s2.hasBreak():
                if week < s2.getWeek(s2.springBreak[0] + timedelta(days=7)):
                    return s2.firstDay - s1.firstDay
                else:
                    return s2.firstDay - s1.firstDay + timedelta(days=7)
            else:
                return s2.firstDay - s1.firstDay

    def getSemester(self, d):
        """Returns the Semester that the date d falls in or None if the date is outside all the semesters."""
        if d is None:
            return None
        for s in self.semesters:
            semester = self.semesters[s]
            if semester.isInSemester(d):
                return semester
        return None
