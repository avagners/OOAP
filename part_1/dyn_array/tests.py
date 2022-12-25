import unittest
import random

from DynArray import DynArray


class TestOneItemDynArray(unittest.TestCase):

    def setUp(self):
        self.d_array = DynArray()
        self.d_array.append(1)
        self.len = self.d_array.count
        self.capacity = self.d_array.capacity
        self.min_capacity = 16

    def test_one_item_check_d_array(self):
        self.assertEqual(self.d_array.count, 1)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_one_item_insert(self):
        new_item = random.randint(0, 100)
        self.assertEqual(self.d_array._insert_status, 0)
        self.d_array.insert(0, new_item)
        self.assertEqual(self.d_array._insert_status, 1)
        self.d_array.insert(self.d_array.count + 1, new_item)
        self.assertEqual(self.d_array._insert_status, 2)
        self.assertEqual(self.d_array.count, self.len + 1)
        self.assertEqual(self.d_array[0], new_item)
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_one_item_remove(self):
        self.assertEqual(self.d_array._remove_status, 0)
        self.d_array.remove(0)
        self.assertEqual(self.d_array._remove_status, 1)
        self.assertEqual(self.d_array.count, self.len - 1)
        self.d_array.remove(0)
        self.assertEqual(self.d_array._remove_status, 2)
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)


class TestEmptyDynArray(unittest.TestCase):

    def setUp(self):
        self.d_array = DynArray()
        self.len = self.d_array.count
        self.capacity = self.d_array.capacity
        self.min_capacity = 16

    def test_empty_check_d_array(self):
        self.assertEqual(self.d_array.count, 0)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_empty_insert(self):
        new_item = random.randint(0, 100)
        self.assertEqual(self.d_array._insert_status, 0)
        self.d_array.insert(0, new_item)
        self.assertEqual(self.d_array._insert_status, 1)
        self.assertEqual(self.d_array.count, self.len + 1)
        self.assertEqual(self.d_array[0], new_item)
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_empty_remove(self):
        self.assertEqual(self.d_array._remove_status, 0)
        self.d_array.remove(0)
        self.assertEqual(self.d_array._remove_status, 2)
        self.assertEqual(self.d_array.count, 0)
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)


class TestManyItemsDynArray(unittest.TestCase):

    def setUp(self):
        self.d_array = DynArray()
        for i in range(16):
            self.d_array.append(i)
        self.len = self.d_array.count
        self.capacity = self.d_array.capacity
        self.min_capacity = 16

    def test_many_items_check_d_array(self):
        self.assertEqual(self.d_array.count, 16)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_many_items_insert_first_place(self):
        new_item = random.randint(0, 100)
        self.assertEqual(self.d_array._insert_status, 0)
        self.d_array.insert(0, new_item)
        self.assertEqual(self.d_array._insert_status, 1)
        self.assertEqual(self.d_array.count, self.len + 1)
        self.assertEqual(self.d_array[0], new_item)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.capacity * 2)

    def test_many_items_insert_last_place(self):
        new_item = random.randint(0, 100)
        self.assertEqual(self.d_array._insert_status, 0)
        self.d_array.insert(self.len, new_item)
        self.assertEqual(self.d_array._insert_status, 1)
        self.assertEqual(self.d_array.count, self.len + 1)
        self.assertEqual(self.d_array[self.len], new_item)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.capacity * 2)

    def test_many_items_insert_middle_place(self):
        new_item = random.randint(0, 100)
        self.assertEqual(self.d_array._insert_status, 0)
        self.d_array.insert(1, new_item)
        self.assertEqual(self.d_array._insert_status, 1)
        self.assertEqual(self.d_array.count, self.len + 1)
        self.assertEqual(self.d_array[1], new_item)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.capacity * 2)

    def test_many_items_remove_first_place(self):
        self.assertEqual(self.d_array._remove_status, 0)
        self.d_array.remove(0)
        self.assertEqual(self.d_array._remove_status, 1)
        self.assertEqual(self.d_array.count, self.len - 1)
        self.assertEqual(self.d_array.capacity, self.capacity)

    def test_many_items_remove_last_place(self):
        self.assertEqual(self.d_array._remove_status, 0)
        self.d_array.remove(self.len - 1)
        self.assertEqual(self.d_array._remove_status, 1)
        self.assertEqual(self.d_array.count, self.len - 1)
        self.assertEqual(self.d_array.capacity, self.capacity)

    def test_many_items_remove_middle_place(self):
        self.assertEqual(self.d_array._remove_status, 0)
        self.d_array.remove(1)
        self.assertEqual(self.d_array._remove_status, 1)
        self.assertEqual(self.d_array.count, self.len - 1)
        self.assertEqual(self.d_array.capacity, self.capacity)

    def test_many_items_raises(self):
        new_item = random.randint(0, 100)
        self.assertEqual(self.d_array._insert_status, 0)
        self.d_array.insert(-1, new_item)
        self.assertEqual(self.d_array._insert_status, 2)
        self.assertEqual(self.d_array._remove_status, 0)
        self.d_array.remove(-1)
        self.assertEqual(self.d_array._remove_status, 2)

    def test_decrease_buffer_size(self):
        new_item = random.randint(0, 100)
        self.d_array.append(new_item)
        self.assertEqual(self.d_array.count, self.len + 1)
        self.assertGreater(self.d_array.count, self.capacity)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        new_capacity = self.capacity * 2
        self.assertEqual(self.d_array.capacity, new_capacity)
        self.d_array.remove(0)
        self.assertGreaterEqual(
            self.d_array.count, self.d_array.capacity * 0.5
        )
        self.assertEqual(self.d_array.capacity, new_capacity)
        self.d_array.remove(0)
        self.assertLess(self.d_array.count, new_capacity * 0.5)
        self.assertEqual(self.d_array.capacity, int(new_capacity / 1.5))

    def test_min_capacity(self):
        half_capacity_plus_one = int(self.d_array.capacity * 0.5) + 1
        for _ in range(half_capacity_plus_one):
            self.d_array.remove(0)
        self.assertEqual(
            self.d_array.count, self.len - half_capacity_plus_one
        )
        self.assertEqual(self.d_array.capacity, self.min_capacity)


if __name__ == '__main__':
    unittest.main()
