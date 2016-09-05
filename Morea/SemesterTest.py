import unittest

from datetime import datetime, timedelta

from Semester import Semester
from SemesterFactory import SemesterFactory

class SemesterTest(unittest.TestCase):

    def testIsInSemester(self):
        s = SemesterFactory().semesters['s16']
        d = datetime.strptime("2016-02-15", '%Y-%m-%d')
        self.assertTrue(s.isInSemester(d))

    def testGetWeek(self):
        s = SemesterFactory().semesters['s16']
        d = datetime.strptime("2016-02-15", '%Y-%m-%d')
        self.assertEqual(s.getWeek(d), 6, "expecting 6 got {}".format(s.getWeek(d)))
        delta = timedelta(days=7)
        d = d + delta
        self.assertEqual(s.getWeek(d), 7, "expecting 7 got {}".format(s.getWeek(d)))
        delta = timedelta(days=-14)
        d = d + delta
        self.assertEqual(s.getWeek(d), 5, "expecting 7 got {}".format(s.getWeek(d)))
        delta = timedelta(days=-44)
        d = d + delta
        self.assertEqual(s.getWeek(d), None, "expecting None got {}".format(s.getWeek(d)))
        d = datetime.strptime("2016-03-23", '%Y-%m-%d')
        self.assertEqual(s.getWeek(d), None, "expecting None got {}".format(s.getWeek(d)))
        d = datetime.strptime("2016-03-30", '%Y-%m-%d')
        self.assertEqual(s.getWeek(d), 11, "expecting 11 got {}".format(s.getWeek(d)))
        d = s.lastDay
        self.assertEqual(s.getWeek(d), 16, "expecting 16 got {}".format(s.getWeek(d)))
        d = datetime.strptime("2016-05-09", '%Y-%m-%d')
        self.assertEqual(s.getWeek(d), 17, "expecting 17 got {}".format(s.getWeek(d)))

    def testHasBreak(self):
        s = SemesterFactory().semesters['s16']
        self.assertTrue(s.hasBreak())
        s = SemesterFactory().semesters['f15']
        self.assertFalse(s.hasBreak())

    def testEquality(self):
        s1 = SemesterFactory().semesters['s16']
        s2 = SemesterFactory().semesters['f15']
        self.assertFalse(s1 == s2)
        s3 = SemesterFactory().semesters['f15']
        self.assertTrue(s3 == s2)

if __name__ == '__main__':
    unittest.main()
