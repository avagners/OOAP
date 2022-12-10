import random
import unittest
from string import ascii_letters

from HashTable import HashTable


class TestHashTableEmptySlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_hash = HashTable(self.size)
        self.number = random.randint(3, len(ascii_letters))
        self.string = ''.join(random.sample(ascii_letters, self.number))
        self.empty_slots = [None for _ in range(self.size)]

    def test_check_hash_table_empty_slots(self):
        self.assertIsInstance(self.s_hash, HashTable)
        self.assertEqual(len(self.s_hash.slots), self.size)
        self.assertListEqual(self.s_hash.slots, self.empty_slots)
        for index in range(self.size):
            self.assertIsNone(self.s_hash.slots[index])

    def test_hash_fun_empty_slots(self):
        hash = self.s_hash._hash_fun(self.string)
        check_hash = sum([ord(sym) for sym in self.string]) % self.size
        self.assertEqual(hash, check_hash)
        self.assertEqual(self.s_hash.size(), 0)

    def test_seek_slot_empty_slots(self):
        slot = self.s_hash._seek_slot(self.string)
        self.assertIsInstance(slot, int)
        self.assertEqual(slot, self.s_hash._hash_fun(self.string))

    def test_put_in_empty_slots(self):
        self.assertEqual(self.s_hash.get_put_status(), 0)
        self.assertIsNone(self.s_hash.put(self.string))
        self.assertEqual(self.s_hash.get_put_status(), 1)
        self.assertEqual(self.s_hash.size(), 1)
        self.assertNotEqual(self.s_hash.slots, self.empty_slots)
        self.assertIn(self.string, self.s_hash.slots)

    def test_find_in_empty_slots(self):
        self.assertFalse(self.s_hash.find(self.string))

    def test_remove_in_empty_slots(self):
        self.assertEqual(self.s_hash.get_remove_status(), 0)
        self.assertIsNone(self.s_hash.remove(self.string))
        self.assertEqual(self.s_hash.get_remove_status(), 2)
        self.assertEqual(self.s_hash.size(), 0)


class TestHashTableFullSlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_hash = HashTable(self.size)
        self.number = random.randint(3, len(ascii_letters))
        self.string = ''.join(random.sample(ascii_letters, self.number))
        self.full_slots = []
        for _ in range(self.size):
            number = random.randint(3, len(ascii_letters))
            string = ''.join(random.sample(ascii_letters, number))
            self.full_slots.append(string)
        for index, string in enumerate(self.full_slots):
            self.s_hash.slots[index] = string

    def test_check_hash_table_full_slots(self):
        self.assertIsInstance(self.s_hash, HashTable)
        self.assertEqual(len(self.s_hash.slots), self.size)
        self.assertListEqual(self.s_hash.slots, self.full_slots)
        for index in range(self.size):
            self.assertIsNotNone(self.s_hash.slots[index])

    def test_hash_fun_full_slots(self):
        hash = self.s_hash._hash_fun(self.string)
        check_hash = sum([ord(sym) for sym in self.string]) % self.size
        self.assertEqual(hash, check_hash)

    def test_seek_slot_full_slots(self):
        slot = self.s_hash._seek_slot(self.string)
        self.assertIsNone(slot)
        self.assertNotEqual(slot, self.s_hash._hash_fun(self.string))

    def test_put_in_full_slots(self):
        self.assertEqual(self.s_hash.get_put_status(), 0)
        self.assertIsNone(self.s_hash.put(self.string))
        self.assertEqual(self.s_hash.get_put_status(), 2)
        self.assertListEqual(self.s_hash.slots, self.full_slots)

    def test_find_in_full_slots(self):
        string = random.choice(self.s_hash.slots)
        self.assertTrue(self.s_hash.find(string))

    def test_find_return_none_in_full_slots(self):
        self.assertFalse(self.s_hash.find('string_not_exist'))

    def test_remove_from_full_slots(self):
        string = random.choice(self.s_hash.slots)
        self.assertNotIn(None, self.s_hash.slots)
        self.assertEqual(self.s_hash.get_remove_status(), 0)
        self.assertIsNone(self.s_hash.remove(string))
        self.assertEqual(self.s_hash.get_remove_status(), 1)
        self.assertIn(None, self.s_hash.slots)


class TestHashTableOneItem(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_hash = HashTable(self.size)
        self.number = random.randint(3, len(ascii_letters))
        self.string = ''.join(random.sample(ascii_letters, self.number))
        self.hash = self.s_hash._hash_fun(self.string)
        self.list_slots = [None for _ in range(self.size)]
        self.list_slots[self.hash] = self.string
        self.s_hash.put(self.string)

    def test_check_hash_table_one_item(self):
        self.assertIsInstance(self.s_hash, HashTable)
        self.assertEqual(len(self.s_hash.slots), self.size)
        self.assertListEqual(self.s_hash.slots, self.list_slots)
        self.assertEqual(self.s_hash.size(), 1)

    def test_hash_fun_one_item(self):
        hash = self.s_hash._hash_fun(self.string)
        check_hash = sum([ord(sym) for sym in self.string]) % self.size
        self.assertEqual(hash, check_hash)

    def test_seek_slot_same_string_one_item(self):
        slot = self.s_hash._seek_slot(self.string)
        self.assertIsNotNone(slot)
        self.assertIsInstance(slot, int)
        self.assertNotEqual(slot, self.s_hash._hash_fun(self.string))
        next_index = (
            self.s_hash._hash_fun(self.string) + self.s_hash._step
        ) % self.size
        self.assertEqual(slot, next_index)

    def test_seek_slot_another_string_one_item(self):
        new_string = self.string + 'x'
        hash_new_string = self.s_hash._hash_fun(new_string)
        hash_old_string = self.s_hash._hash_fun(self.string)
        slot = self.s_hash._seek_slot(new_string)
        self.assertIsNotNone(slot)
        self.assertIsInstance(slot, int)
        self.assertNotEqual(hash_new_string, hash_old_string)

    def test_put_same_string_one_item(self):
        self.assertEqual(self.s_hash.get_put_status(), 1)
        self.assertIsNone(self.s_hash.put(self.string))
        self.assertEqual(self.s_hash.get_put_status(), 1)
        self.assertEqual(self.s_hash.size(), 2)

    def test_put_another_string_one_item(self):
        new_string = self.string + 'x'
        hash_new_string = self.s_hash._hash_fun(new_string)
        hash_old_string = self.s_hash._hash_fun(self.string)
        self.assertEqual(self.s_hash.get_put_status(), 1)
        self.assertIsNone(self.s_hash.put(new_string))
        self.assertEqual(self.s_hash.get_put_status(), 1)
        self.assertEqual(self.s_hash.size(), 2)
        self.assertNotEqual(hash_new_string, hash_old_string)
        self.assertIn(new_string, self.s_hash.slots)

    def test_find_in_one_item(self):
        self.assertTrue(self.s_hash.find(self.string))

    def test_find_return_none_in_one_item(self):
        self.assertFalse(self.s_hash.find('string_not_exist'))


if __name__ == '__main__':
    unittest.main()
