from Entity import Types
from datetime import timedelta
from SemesterFactory import SemesterFactory


class MoveClassInstance(object):
    """Moves a class instance from one semester to another. This updates the files inplace."""

    def __init__(self, ci, newSemester, weekDays=None, semesterPath=None):
        """Creates a new instance with the ClassInstance, newSemester and optional weekDays. If weekDays is not None,
        the the class meetings will be updated to the new weekDays ('MW' or 'TR')."""
        self.factory = SemesterFactory(semesterPath)
        self.classInstance = ci
        self.oldSemester = ci.getSemester()
        self.newSemester = newSemester
        self.moveDay = False
        self.moveToMW = False
        self.moveToTR = False
        if weekDays is not None:
            if ci.isMW() and weekDays == 'TR':
                self.moveToMW = False
                self.moveToTR = True
                self.moveDay = True
            elif ci.isTR() and weekDays == 'MW':
                self.moveToMW = True
                self.moveToTR = False
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
            elif self.moveDay and self.moveToTR:
                offset = 1
            elif self.moveDay and self.moveToMW:
                offset = -1
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
        if self.moveToMW:
            moveDay = "TR to MW"
        if self.moveToTR:
            moveDay = "MW to TR"
        return "MoveClassInstance [{0} -> {1} {2}]".format(self.classInstance.getSemester().name, self.newSemester.name,
                                                           moveDay)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def moveClassInstance(ci, newSemester, weekDays=None):
        """Moves the class instance ci from its current semester to the newSemester. If weekDays is not None will
        update the class meetings to the new weekDays ('MW' or 'TR')"""
        s1 = ci.getSemester()
        mw = ci.isMW()
        tr = ci.isTR()
        dayOffset = 0
        if weekDays != None:
            if mw and weekDays == 'TR':
                dayOffset = 1
            elif tr and weekDays == 'MW':
                dayOffset = -1
                # for m in ci.entities[Types.module.name]:
                #     MoveClassInstance.moveEntity(m, s1, newSemester, dayOffset)
                # for r in ci.entities[Types.reading.name]:
                # MoveClassInstance.moveEntity(r, s1, newSemester, dayOffset)
        for e in ci.entities[Types.experience.name]:
            MoveClassInstance.moveEntity(e, s1, newSemester, dayOffset)

    @staticmethod
    def moveEntity(entity, oldSemester, newSemester, dayOffset):
        factory = SemesterFactory()
        week = oldSemester.getWeek(entity.startDate)
        if week is None:
            week = oldSemester.getWeek(entity.endDate)
        delta = factory.getDelta(oldSemester, newSemester, week)
        offset = timedelta(days=dayOffset)
        if entity.startsMonThur():
            delta = delta + offset
        if entity.startDate is not None:
            newStart = entity.startDate + delta
            print week, entity.title, entity.startDate.isoweekday(), newStart.isoweekday()

