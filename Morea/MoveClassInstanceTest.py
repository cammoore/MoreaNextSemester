import unittest
from ClassInstance import ClassInstance
from MoveClassInstance import MoveClassInstance
from SemesterFactory import SemesterFactory


class MoveClassInstanceTest(unittest.TestCase):

    def testIsInstance(self):
        instance = ClassInstance('../testing/ics111/morea/')
        factory = SemesterFactory()
        newSemester = factory.getSemesterFromName('s17')
        MoveClassInstance.moveClassInstance(instance, newSemester, 'MW')

if __name__ == '__main__':
    unittest.main()
