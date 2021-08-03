import getopt
import sys

from Morea.ClassInstance import ClassInstance
from Morea.MoveClassInstanceSemToSem import MoveClassInstanceSemToSem
from Morea.SemesterFactory import SemesterFactory


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "h", ["help"])
        for o, a in opts:
            if o in ("-h", "--help"):
                print("Usage: python MoreaNextSemester.py <directory> <semester> <dayOfWeek:Optional>")
                print("  directory should be to your morea/ directory in the master branch")
                print("  semester should be [s|f]YY, e.g. ('s17' or 'f18')")
                print("  dayOfWeek is optional and must be either 'MW' or 'TR'")
                print("   eg: python MoreaNextSemester.py ~/Morea/ics211f16/master/src/morea/ f16")
                return 0

        if len(args) < 2:
            print("Usage: python MoreaNextSemester.py <morea-directory> <old semester> <new semester> <dayOfWeek:Optional>")
            print("   eg: python MoreaNextSemester.py ~/Morea/ics211f16/master/src/morea/ f16 s17 TR")
            return 2

        semesterPath = './Morea/uh-semesters.json'
        instance = ClassInstance(args[0], semesterPath)
        print("Starting instance = {}".format(instance))
        factory = SemesterFactory(semesterPath)
        oldSemester = factory.getSemesterFromName(args[1])
        newSemester = factory.getSemesterFromName(args[2])
        weekDay = None
        if len(args) > 3:
            weekDay = args[3]
        mover = MoveClassInstanceSemToSem(instance, oldSemester, newSemester, weekDay, semesterPath)
        mover.moveEntities()
        i2 = ClassInstance(args[0], semesterPath)
        print("Moved instance = {}".format(i2))

    except getopt.error as msg:
        print(msg)
        print("for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
