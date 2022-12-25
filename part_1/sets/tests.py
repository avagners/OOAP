import random
import unittest

from PowerSet import PowerSet


class TestPowerSet(unittest.TestCase):

    def setUp(self):
        self.s_set = PowerSet(16)
        self.items_list = [str(i) for i in range(1, 16)]
        for item in self.items_list:
            self.s_set.put(item)

    def test_put_success(self):
        new_item = '1000001'
        self.assertEqual(self.s_set.size(), len(self.items_list))
        self.assertNotIn(new_item, self.s_set.slots)
        self.s_set.put(new_item)
        self.assertEqual(self.s_set.size(), len(self.items_list) + 1)
        self.assertIn(new_item, self.s_set.slots)

    def test_put_fail(self):
        new_item = random.choice(self.s_set.slots)
        self.assertEqual(self.s_set.size(), len(self.items_list))
        self.assertIn(new_item, self.s_set.slots)
        self.s_set.put(new_item)
        self.assertEqual(self.s_set.size(), len(self.items_list))
        self.assertIn(new_item, self.s_set.slots)

    def test_remove_true(self):
        item = random.choice(self.s_set.slots)
        self.assertEqual(self.s_set.size(), len(self.items_list))
        self.assertIn(item, self.s_set.slots)
        self.s_set.remove(item)
        self.assertEqual(self.s_set.size(), len(self.items_list) - 1)
        self.assertNotIn(item, self.s_set.slots)

    def test_remove_false(self):
        item = '1000001'
        self.assertEqual(self.s_set.size(), len(self.items_list))
        self.assertNotIn(item, self.s_set.slots)
        self.s_set.remove(item)
        self.assertEqual(self.s_set.size(), len(self.items_list))

    def test_intersection_return_empty_set(self):
        set2 = PowerSet(16)
        result = self.s_set.intersection(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertEqual(result.slots, set2.slots)

    def test_intersection_return_set(self):
        set2 = PowerSet(16)
        items_list1 = [str(i) for i in range(10, 20)]
        for i in items_list1:
            set2.put(i)
        result = self.s_set.intersection(set2)
        self.assertIsInstance(result, PowerSet)
        for item in result.slots:
            self.assertIn(item, self.s_set.slots)
            self.assertIn(item, set2.slots)
        self.assertEqual(result.size(), 6)

    def test_union_another_set2(self):
        set2 = PowerSet(16)
        items_list1 = [str(i) for i in range(16, 32)]
        for i in items_list1:
            set2.put(i)
        result = self.s_set.union(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertEqual(result.size(), self.s_set.size() + set2.size())

    def test_union_set2_empty(self):
        set2 = PowerSet(16)
        result = self.s_set.union(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertEqual(result.size(), self.s_set.size())

    def test_union_set2(self):
        set2 = PowerSet(16)
        items_list1 = [str(i) for i in range(1, 16)]
        for i in items_list1:
            set2.put(i)
        result = self.s_set.union(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertLessEqual(result.size(), self.s_set.size())

    def test_union_set2_2(self):
        set2 = PowerSet(16)
        items_list1 = [str(i) for i in range(8, 23)]
        for i in items_list1:
            set2.put(i)
        result = self.s_set.union(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertLessEqual(result.size(), self.s_set.size() + 7)

    def test_difference_another_set2(self):
        set2 = PowerSet(16)
        result = self.s_set.difference(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertEqual(result.slots, self.s_set.slots)

    def test_difference_identical_sets(self):
        set2 = self.s_set
        self.assertListEqual(self.s_set.slots, set2.slots)
        result = self.s_set.difference(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertListEqual(result.slots, [None] * 16)

    def test_difference_sets(self):
        set2 = PowerSet(16)
        items_list1 = [str(i) for i in range(16, 32)]
        for i in items_list1:
            set2.put(i)
        result = self.s_set.difference(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertLessEqual(result.size(), self.s_set.size())
        self.assertEqual(result.slots, self.s_set.slots)

    def test_issubset_identical_sets(self):
        set2 = self.s_set
        self.assertTrue(self.s_set.issubset(set2))

    def test_issubset_not_all_elements_sets(self):
        set2 = PowerSet(16)
        items_list1 = [str(i) for i in range(8, 23)]
        for i in items_list1:
            set2.put(i)
        self.assertFalse(self.s_set.issubset(set2))


if __name__ == '__main__':
    unittest.main()
