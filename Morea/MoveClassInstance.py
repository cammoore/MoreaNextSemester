from Entity import Types
from datetime import timedelta
from SemesterFactory import SemesterFactory


class MoveClassInstance(object):
    """Moves a class instance from one semester to another. This updates the files inplace."""

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

