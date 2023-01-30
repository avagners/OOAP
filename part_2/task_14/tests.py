import unittest

from task_14 import Vector


class TestsVector(unittest.TestCase):

    def setUp(self):
        self.a_obj = Vector([1, 2, 3])
        self.b_obj = Vector([4, 5, 6])

    def test_success(self):
        result = self.a_obj + self.b_obj
        self.assertIsInstance(result, Vector)
        self.assertEqual(result.values, [5, 7, 9])

    def test_not_success(self):
        self.c_obj = Vector([4, 5, 6, 8])
        self.assertIsNone(self.a_obj + self.c_obj)

    def test_vector_of_vectors_addition(self):
        v1 = Vector([Vector([1, 2, 3]), Vector([4, 5, 6])])
        v2 = Vector([Vector([7, 8, 9]), Vector([10, 11, 12])])
        v3 = v1 + v2
        self.assertIsInstance(v3, Vector)
        self.assertIsInstance(v3.values, list)
        check_value = [[8, 10, 12], [14, 16, 18]]
        for index, item in enumerate(v3.values):
            self.assertIsInstance(item, Vector)
            self.assertIsInstance(item.values, list)
            self.assertListEqual(item.values, check_value[index])
        # проверяем, если длина списков отличается
        v4 = Vector([Vector([1, 2, 3]), Vector([4, 5])])
        v5 = v1 + v4
        self.assertIsInstance(v5, Vector)
        self.assertIsInstance(v5.values, list)
        self.assertIsInstance(v5.values[0], Vector)
        self.assertEqual(v5.values[0].values, [2, 4, 6])
        self.assertIsNone(v5.values[1])  # второе значение None,
        # так длина список отличается


if __name__ == '__main__':
    unittest.main()
