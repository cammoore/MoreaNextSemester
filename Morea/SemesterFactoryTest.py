import getopt
import sys

from SemesterFactory import SemesterFactory


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "h", ["help"])
        for o, a in opts:
            if o in ("-h", "--help"):
                print >>sys.stdout, "Usage: python SemesterFactoryTest.py <json-file>"
                return 0

        if len(args) < 1:
            print >>sys.stderr, "Usage: python ClassInstanceTest.py <json-file>"
            return 2

        factory = SemesterFactory(args[0])
        print factory.semesters
        # print factory.buildSemesters(args[0])

    except getopt.error, msg:
        print >>sys.stderr, msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())

