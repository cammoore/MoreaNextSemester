import getopt
import sys

from Morea.ClassInstance import ClassInstance
from Morea.MoveClassInstanceToFriday import MoveClassInstanceToFriday
from Morea.SemesterFactory import SemesterFactory


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "h", ["help"])
        for o, a in opts:
            if o in ("-h", "--help"):
                print >>sys.stdout, "Usage: python MoreaNextSemester.py <directory> <semester>"
                print >>sys.stdout, "  directory should be to your morea/ directory in the master branch"
                print >>sys.stdout, "  semester should be [s|f]YY, e.g. ('s17' or 'f18')"
                print >>sys.stdout, "   eg: python MoreaNextSemesterOnFridays.py ~/Morea/ics211f16/master/src/morea/ f16"
                return 0

        if len(args) < 2:
            print >>sys.stderr, "Usage: python MoreaNextSemester.py <morea-directory> <semester> <dayOfWeek:Optional>"
            print >>sys.stderr, "   eg: python MoreaNextSemester.py ~/Morea/ics211f16/master/src/morea/ f16"
            return 2

        semesterPath = './Morea/uh-semesters.json'
        instance = ClassInstance(args[0], semesterPath)
        print "Starting instance = {}".format(instance)
        factory = SemesterFactory(semesterPath)
        newSemester = factory.getSemesterFromName(args[1])
        mover = MoveClassInstanceToFriday(instance, newSemester, semesterPath)
        mover.moveEntities()
        i2 = ClassInstance(args[0], semesterPath)
        print "Moved instance = {}".format(i2)

    except getopt.error, msg:
        print >>sys.stderr, msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
