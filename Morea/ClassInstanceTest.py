import getopt
import sys

from ClassInstance import ClassInstance
from Entity import Types


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "h", ["help"])
        for o, a in opts:
            if o in ("-h", "--help"):
                print >>sys.stdout, "Usage: python ClassInstanceTest.py <directory>"
                return 0

        if len(args) < 1:
            print >>sys.stderr, "Usage: python ClassInstanceTest.py <directory>"
            return 2
        instance = ClassInstance(args[0])
        print ("{0} modules | {1} outcomes | {2} readings | {3} experiences | {4} assessments ".format(instance.getNumModules(),
                                                                                                      instance.getNumOutcomes(),
                                                                                                      instance.getNumReadings(),
                                                                                                      instance.getNumExperiences(),
                                                                                                      instance.getNumAssessments()))
        # for e in instance.entities["experience"]:
        #     print e.title, e.getStartWeekDay()
        # print instance.readingDays
        for r in instance.entities[Types.reading.name]:
            if r.startsOnFriday():
                print(r)
        for e in instance.entities[Types.experience.name]:
            if e.startsOnFriday():
                print(e)
        # print instance.experienceDays
        print(instance.getMeetingDays())
        # print instance.homeworks
        print('Start Date', instance.startDate)
        print(instance.getSemester().getShortName())
        print('is MW', instance.isMW())
        print('is TR', instance.isTR())
        # for m in instance.entities[Types.module.name]:
        #     print m, m.startsOnSaturday(), m.endsOnFriday(), m.getDurationInDays()


    except getopt.error, msg:
        print >>sys.stderr, msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
