import random
import unittest
from string import ascii_letters

from NativeDictionary import NativeDictionary


class TestNativeDictEmptySlots(unittest.TestCase):

    def setUp(self):
        self.s_dict = NativeDictionary()
        self.size = 16
        self.number = random.randint(3, len(ascii_letters))
        self.key = ''.join(random.sample(ascii_letters, self.number))
        self.value = ''.join(random.sample(ascii_letters, self.number))
        self.empty_slots = [None] * 16

    def test_check_native_dict(self):
        self.assertIsInstance(self.s_dict, NativeDictionary)
        self.assertEqual(len(self.s_dict._slots), self.size)
        self.assertEqual(len(self.s_dict._values), self.size)
        self.assertListEqual(self.s_dict._slots, self.empty_slots)
        self.assertListEqual(self.s_dict._values, self.empty_slots)
        for index in range(self.size):
            self.assertIsNone(self.s_dict._slots[index])
            self.assertIsNone(self.s_dict._values[index])

    def test_is_key_empty_slots(self):
        self.assertFalse(self.s_dict.is_key(self.key))

    def test_put_in_empty_slots(self):
        self.assertEqual(self.s_dict.get_put_status(), 0)
        self.assertIsNone(self.s_dict.put(self.key, self.value))
        self.assertEqual(self.s_dict.get_put_status(), 1)
        self.assertIn(self.key, self.s_dict._slots)
        self.assertIn(self.value, self.s_dict._values)
        self.assertIsNone(self.s_dict.put(self.key, 55))
        self.assertEqual(self.s_dict.get_put_status(), 2)
        self.assertIn(self.key, self.s_dict._slots)
        self.assertNotIn(self.value, self.s_dict._values)

    def test_get_in_empty_slots(self):
        self.assertEqual(self.s_dict.get_get_status(), 0)
        self.assertIsNone(self.s_dict.get(self.key))
        self.assertEqual(self.s_dict.get_get_status(), 2)

    def test_remove_in_empty_slots(self):
        self.assertEqual(self.s_dict.get_remove_status(), 0)
        self.assertIsNone(self.s_dict.remove(self.key))
        self.assertEqual(self.s_dict.get_remove_status(), 2)

    def test_size_in_empty_slots(self):
        self.assertEqual(self.s_dict.size(), 0)


class TestNativeDictFullSlots(unittest.TestCase):

    def setUp(self):
        self.size = 16
        self.s_dict = NativeDictionary()
        self.number = random.randint(3, len(ascii_letters))
        self.new_key = ''.join(random.sample(ascii_letters, self.number))
        self.new_value = ''.join(random.sample(ascii_letters, self.number))
        self.full_keys = []
        self.full_values = []
        for _ in range(self.size):
            number = random.randint(3, len(ascii_letters))
            key = ''.join(random.sample(ascii_letters, number))
            value = ''.join(random.sample(ascii_letters, number))
            self.s_dict.put(key, value)

    def test_check_native_dict_full_slots(self):
        self.assertIsInstance(self.s_dict, NativeDictionary)
        self.assertEqual(len(self.s_dict._slots), self.size)
        self.assertEqual(len(self.s_dict._values), self.size)
        self.assertNotIn(None, self.s_dict._slots)
        self.assertNotIn(None, self.s_dict._values)
        for index in range(self.size):
            self.assertIsNotNone(self.s_dict._slots[index])
            self.assertIsNotNone(self.s_dict._values[index])

    def test_is_key_full_slots(self):
        self.assertFalse(self.s_dict.is_key(self.new_key))
        self.assertTrue(self.s_dict.is_key(self.s_dict._slots[0]))

    def test_put_in_full_slots(self):
        self.assertEqual(len(self.s_dict._slots), self.size)
        self.assertEqual(len(self.s_dict._values), self.size)
        self.assertEqual(self.s_dict.get_put_status(), 1)
        self.assertIsNone(self.s_dict.put(self.new_key, self.new_value))
        self.assertEqual(self.s_dict.get_put_status(), 1)
        self.assertIn(self.new_key, self.s_dict._slots)
        self.assertIn(self.new_value, self.s_dict._values)
        self.assertEqual(self.s_dict.size(), self.size + 1)
        self.assertEqual(len(self.s_dict._slots), self.size * 2)
        self.assertEqual(len(self.s_dict._values), self.size * 2)

    def test_get_in_full_slots(self):
        self.assertEqual(self.s_dict.get_get_status(), 0)
        self.assertIsNone(self.s_dict.get(self.new_key))
        self.assertEqual(self.s_dict.get_get_status(), 2)
        self.assertEqual(self.s_dict.get_put_status(), 1)
        self.assertIsNone(self.s_dict.put(self.new_key, self.new_value))
        self.assertEqual(self.s_dict.get_put_status(), 1)
        self.assertEqual(self.s_dict.get_get_status(), 2)
        self.assertEqual(self.s_dict.get(self.new_key), self.new_value)
        self.assertEqual(self.s_dict.get_get_status(), 1)

    def test_remove_in_empty_slots(self):
        self.assertEqual(self.s_dict.get_remove_status(), 0)
        self.assertIsNone(self.s_dict.remove(self.new_key))
        self.assertEqual(self.s_dict.get_remove_status(), 2)
        self.assertEqual(len(self.s_dict._slots), self.size)
        self.assertEqual(self.s_dict.size(), self.size)
        self.assertEqual(self.s_dict.get_put_status(), 1)
        self.assertIsNone(self.s_dict.put(self.new_key, self.new_value))
        self.assertEqual(self.s_dict.get_put_status(), 1)
        self.assertEqual(self.s_dict.size(), self.size + 1)
        self.assertEqual(len(self.s_dict._slots), self.size * 2)
        self.assertEqual(self.s_dict.get_remove_status(), 2)
        self.assertIsNone(self.s_dict.remove(self.new_key))
        self.assertEqual(self.s_dict.get_remove_status(), 1)
        self.assertEqual(self.s_dict.size(), self.size)
        self.assertEqual(len(self.s_dict._slots), self.size * 2)
        self.assertEqual(len(self.s_dict._values), self.size * 2)
        keys_to_remove = self.s_dict._slots[:9]
        self.assertIsNone(self.s_dict.remove(keys_to_remove[0]))
        self.assertIsNone(self.s_dict.remove(keys_to_remove[1]))
        self.assertEqual(self.s_dict.size(), self.size - 2)
        self.assertEqual(len(self.s_dict._slots), int(self.size * 2 / 1.5))
        self.assertEqual(len(self.s_dict._values), int(self.size * 2 / 1.5))
        for key in keys_to_remove[2:]:
            self.assertIsNone(self.s_dict.remove(key))
            self.assertEqual(self.s_dict.get_remove_status(), 1)
        self.assertEqual(self.s_dict.size(), self.size - len(keys_to_remove))
        self.assertEqual(len(self.s_dict._slots), self.size)
        self.assertEqual(len(self.s_dict._values), self.size)

    def test_size_in_empty_slots(self):
        self.assertEqual(self.s_dict.size(), self.size)


if __name__ == '__main__':
    unittest.main()
