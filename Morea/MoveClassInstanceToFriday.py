from Entity import Types
from datetime import timedelta
from SemesterFactory import SemesterFactory


class MoveClassInstanceToFriday(object):
    """Moves a class instance from one semester to another and pushes them to Fridays. This updates the files inplace."""

    def __init__(self, ci, newSemester, semesterPath=None):
        """Creates a new instance with the ClassInstance, newSemester. The the class meetings will be updated to
        the Friday of the new week."""
        self.factory = SemesterFactory(semesterPath)
        self.classInstance = ci
        self.oldSemester = ci.getSemester()
        self.newSemester = newSemester
        self.moveDay = False
        if ci.isMW() or ci.isTR():
            self.moveDay = True

    def dayOffset(self, entity):
        """Calculates the day offset for the given entity."""
        if entity.hasDate():
            offset = 0
            if entity.type == Types.experience.name and entity.isDueFridayEvening():
                # Don't move homework assignments which are due on Friday evenings
                offset = 0
            elif entity.type == Types.module.name and entity.startsOnSaturday():
                # Don't move modules that are a multiple of weeks long
                offset = 0
            elif self.moveDay:
                offset = 5 - entity.getStartWeekDay()
            return timedelta(days=offset)
        return None

    def semesterOffset(self, entity):
        """Calculates the semester offset for the given entity. This takes into account the week of the semester."""
        if entity.hasDate():
            week = self.oldSemester.getWeek(entity.startDate)
            if week is None:
                week = self.oldSemester.getWeek(entity.endDate)
            semOffset = self.factory.getDelta(self.oldSemester, self.newSemester, week)
            return semOffset
        return None

    def moveEntities(self):
        """Moves all the entities in the ClassInstance to the new Semester and weekDay."""
        for key in self.classInstance.entities:
            for e in self.classInstance.entities[key]:
                if e.hasDate():
                    sOffset = self.semesterOffset(e)
                    dOffset = self.dayOffset(e)
                    e.updateFileDates(sOffset + dOffset)

    def __str__(self):
        moveDay = "Same day"
        if self.moveDay:
            moveDay = "to F"
        return "MoveClassInstanceToFriday [{0} -> {1} {2}]".format(self.classInstance.getSemester().name, self.newSemester.name,
                                                           moveDay)

    def __repr__(self):
        return self.__str__()
