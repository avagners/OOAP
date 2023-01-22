import unittest

from task_9 import Any, General


class Tests(unittest.TestCase):

    def setUp(self):
        self.a_obj = Any(content=[1, 2, 3], name='Jack')
        self.b_obj = Any()

    def test_copy_attr(self):
        self.assertNotEqual(self.a_obj.__dict__, self.b_obj.__dict__)
        self.assertEqual(self.b_obj.__dict__, {})
        self.a_obj.copy(other=self.b_obj)
        self.assertIsNotNone(self.b_obj.__dict__)
        self.assertEqual(self.a_obj.__dict__, self.b_obj.__dict__)

    def test_clone_obj(self):
        c_obj = self.a_obj.clone()
        self.assertIsInstance(c_obj, Any)
        self.assertEqual(c_obj.__dict__, self.a_obj.__dict__)

    def test_is_type(self):
        self.assertTrue(self.a_obj.is_type(Any))
        self.assertTrue(self.b_obj.is_type(Any))
        self.assertFalse(self.a_obj.is_type(General))
        self.assertFalse(self.b_obj.is_type(General))

    def test_get_type(self):
        self.assertEqual(self.a_obj.type(), Any.__name__)
        self.assertIsInstance(self.a_obj.type(), str)
        self.assertEqual(self.b_obj.type(), Any.__name__)
        self.assertIsInstance(self.b_obj.type(), str)

    def test_print_attr(self):
        self.assertIsInstance(self.a_obj.attributes(), str)
        self.assertEqual(
            self.a_obj.attributes(),
            "attributes: {'content': [1, 2, 3], 'name': 'Jack'}"
        )
        self.assertIsInstance(self.b_obj.attributes(), str)
        self.assertEqual(
            self.b_obj.attributes(),
            "attributes: {}"
        )

    def test_serialize_deserialize(self):
        serialized_obj: bytes = self.a_obj.serialize()
        self.assertIsInstance(serialized_obj, bytes)
        deserialized_obj: Any = self.a_obj.deserialize(serialized_obj)
        self.assertIsInstance(deserialized_obj, Any)
        self.assertEqual(deserialized_obj.__dict__, self.a_obj.__dict__)

    def test_eq(self):
        self.assertFalse(self.a_obj.__eq__(self.b_obj))
        self.a_obj.copy(other=self.b_obj)
        self.assertTrue(self.a_obj.__eq__(self.b_obj))
        c_obj = self.a_obj.clone()
        self.assertTrue(self.a_obj.__eq__(c_obj))


if __name__ == '__main__':
    unittest.main()
