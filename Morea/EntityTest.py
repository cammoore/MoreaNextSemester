import unittest
from Entity import Entity, Types


class EntityTest(unittest.TestCase):

    def testEquality(self):
        id = 'experience-practice-quiz'
        title = 'Q01: Practice Quiz'
        type = Types.assessment.name
        file_name = '../testing/ics111/morea/010.introduction/experience-practice-quiz.md'
        file_name2 = '../testing/orig/ics111/morea/010.introduction/experience-practice-quiz.md'
        startDate = None
        endDate = None
        e1 = Entity(id, title, type, file_name, startDate, endDate)
        e2 = Entity(id, title, type, file_name, startDate, endDate)
        self.assertTrue(e1 == e2)
        e3 = Entity(id, title, type, file_name2, startDate, endDate)
        self.assertTrue(e1 == e3)
        e4 = Entity(id, title, Types.experience.name, file_name2, startDate, endDate)
        self.assertFalse(e3 == e4)

if __name__ == '__main__':
    unittest.main()
