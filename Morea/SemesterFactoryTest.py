import unittest

from datetime import timedelta

from SemesterFactory import SemesterFactory


class SemesterFactoryTest(unittest.TestCase):

    def testDefault(self):
        factory = SemesterFactory()
        self.assertIsNotNone(factory)
        ans = len(factory.semesters.keys())
        self.assertEqual(ans, 8, "expecting 8 got {}".format(ans))

    def testPath(self):
        factory = SemesterFactory("./uh-semesters2.json")
        self.assertIsNotNone(factory)
        ans = len(factory.semesters.keys())
        self.assertEqual(ans, 4, "expecting 4 got {}".format(ans))

    def testDelta(self):
        factory = SemesterFactory()
        self.assertIsNotNone(factory)
        s1 = factory.semesters['s16']
        s2 = factory.semesters['s16']
        for w in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
            delta = factory.getDelta(s1, s2, w)
            self.assertEqual(delta.days, 0)
        s2 = factory.semesters['f16']
        ans = (s2.firstDay - s1.firstDay).days
        for w in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            delta = factory.getDelta(s1, s2, w)
            self.assertEqual(delta.days, ans, "s16 -> f16 week {} expected {} got {}".format(w, ans, delta.days))
        ans = (s2.firstDay - s1.firstDay).days - 7
        for w in [11, 12, 13, 14, 15, 16]:
            delta = factory.getDelta(s1, s2, w)
            self.assertEqual(delta.days, ans, "s16 -> f16 week {} expected {} got {}".format(w, ans, delta.days))
        s1 = factory.semesters['f15']
        s2 = factory.semesters['s16']
        for w in [1, 10, 11, 12]:
            delta = factory.getDelta(s1, s2, w)
            if w < s2.getWeek(s2.springBreak[0] + timedelta(days=7)):
                self.assertEqual(delta.days, 140, "week {} expected  got {}".format(w, delta.days))
            else:
                self.assertEqual(delta.days, 147, "week {} expected  got {}".format(w, delta.days))



if __name__ == '__main__':
    unittest.main()

