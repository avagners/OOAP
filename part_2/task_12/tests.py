import unittest

from task_12 import FirstClass, SecondClass


class Tests(unittest.TestCase):

    def setUp(self):
        self.a_obj = FirstClass(content=[1, 2, 3], name='Jack')
        self.b_obj = SecondClass()
        self.c_obj = FirstClass()

    def test_assignment_attempt(self):
        self.assertNotEqual(self.c_obj.__dict__, self.a_obj.__dict__)
        self.c_obj = self.c_obj.assignment_attempt(self.c_obj, self.a_obj)
        self.assertEqual(self.c_obj.__dict__, self.a_obj.__dict__)
        self.assertNotEqual(self.b_obj.__dict__, self.a_obj.__dict__)
        self.b_obj = self.b_obj.assignment_attempt(self.b_obj, self.a_obj)
        self.assertIsInstance(self.b_obj, None)


if __name__ == '__main__':
    unittest.main()
