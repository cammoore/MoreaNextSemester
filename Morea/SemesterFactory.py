import json

from datetime import datetime
from Semester import Semester

class SemesterFactory(object):

    def __init__(self, filePath):
        """Create a new instance"""
        self.filePath = filePath
        self.semesters = {}
        for s in self.buildSemesters(self.filePath):
            self.semesters[self.shortName(s.name)] = s


    def shortName(self, semesterName):
        return semesterName[:1].lower() + semesterName[len(semesterName) - 2:]



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
