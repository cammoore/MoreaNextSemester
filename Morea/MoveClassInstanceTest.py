import unittest
from ClassInstance import ClassInstance
from Entity import Types
from MoveClassInstance import MoveClassInstance
from SemesterFactory import SemesterFactory


class MoveClassInstanceTest(unittest.TestCase):

    def testIsInstance(self):
        instance = ClassInstance('../testing/ics111/morea/')
        factory = SemesterFactory()
        newSemester = factory.getSemesterFromName('s17')
        mover = MoveClassInstance(instance, newSemester, 'MW')
        self.assertIsNotNone(mover, "Failed to create the MoveClassInstance")
        print mover

    def testCIEquals(self):
        i1 = ClassInstance('../testing/ics111/morea/')
        i2 = ClassInstance('../testing/ics211/morea/')
        self.assertFalse(i1 == i2)
        i3 = ClassInstance('../testing/orig/ics211/morea/')
        self.assertTrue(i2 == i3)

    def testMove(self):
        instance = ClassInstance('../testing/ics111/morea/')
        factory = SemesterFactory()
        newSemester = factory.getSemesterFromName('s17')
        mover = MoveClassInstance(instance, newSemester, 'MW')
        mover.moveEntities()
        instance = ClassInstance('../testing/ics111/morea/')
        self.assertTrue(instance.getSemester() == newSemester)
        print instance
        newSemester = factory.getSemesterFromName('f16')
        mover = MoveClassInstance(instance, newSemester, 'TR')
        mover.moveEntities()
        i1 = ClassInstance('../testing/ics111/morea/')
        i2 = ClassInstance('../testing/orig/ics111/morea/')
        self.assertEqual(i1, i2)

if __name__ == '__main__':
    unittest.main()
