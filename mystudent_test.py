#mystudent_test.py
import unittest
from my_student import Student2


class TestStudent(unittest.TestCase):

    def test_90_to_100(self):
        s1 = Student2('hong',95)
        s2 = Student2('li',100)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')
    def test_60_to_89(self):
        s1 = Student2('chen',60)
        s2 = Student2('hua',75)
        self.assertEqual(s1.get_grade(),'B')
        self.assertEqual(s2.get_grade(),'B')
    def test_0_to_60(self):
        s1 = Student2('ke',30)
        s2 = Student2('jie',50)
        self.assertEqual(s1.get_grade(),'C')
        self.assertEqual(s2.get_grade(),'C')
    def test_invalid(self):
        s1 = Student2('bob',120)
        s2 = Student2('jack',-22)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
