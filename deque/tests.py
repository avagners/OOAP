import random
import unittest

from Deque import Deque


class TestDequeOneItem(unittest.TestCase):

    def setUp(self):
        self.s_deque = Deque()
        self.number = random.randint(0, 100)
        self.s_deque.add_tail(self.number)

    def test_one_item_size(self):
        self.assertEqual(self.s_deque.size(), 1)

    def test_one_item_add_tail(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.add_tail(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[-1], new_item)
        self.assertEqual(self.s_deque.get_get_front_status(), 0)
        self.assertEqual(self.s_deque.get_front(), self.number)
        self.assertEqual(self.s_deque.get_get_front_status(), 1)
        self.assertEqual(self.s_deque.get_get_tail_status(), 0)
        self.assertEqual(self.s_deque.get_tail(), new_item)
        self.assertEqual(self.s_deque.get_get_tail_status(), 1)

    def test_one_item_add_front(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.add_front(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[0], new_item)
        self.assertEqual(self.s_deque.get_get_front_status(), 0)
        self.assertEqual(self.s_deque.get_front(), new_item)
        self.assertEqual(self.s_deque.get_get_front_status(), 1)
        self.assertEqual(self.s_deque.get_get_tail_status(), 0)
        self.assertEqual(self.s_deque.get_tail(), self.number)
        self.assertEqual(self.s_deque.get_get_tail_status(), 1)

    def test_one_item_remove_tail(self):
        len_queue = self.s_deque.size()
        self.assertEqual(self.s_deque.get_remove_tail_status(), 0)
        self.assertIsNone(self.s_deque.remove_tail())
        self.assertEqual(self.s_deque.get_remove_tail_status(), 1)
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertListEqual(self.s_deque.deque, [])
        self.assertEqual(self.s_deque.get_remove_tail_status(), 1)
        self.assertIsNone(self.s_deque.remove_tail())
        self.assertEqual(self.s_deque.get_remove_tail_status(), 2)
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertListEqual(self.s_deque.deque, [])

    def test_one_item_remove_front(self):
        len_queue = self.s_deque.size()
        self.assertEqual(self.s_deque.get_remove_front_status(), 0)
        self.assertIsNone(self.s_deque.remove_front())
        self.assertEqual(self.s_deque.get_remove_front_status(), 1)
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertListEqual(self.s_deque.deque, [])
        self.assertEqual(self.s_deque.get_remove_front_status(), 1)
        self.assertIsNone(self.s_deque.remove_front())
        self.assertEqual(self.s_deque.get_remove_front_status(), 2)
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertListEqual(self.s_deque.deque, [])


class TestDequeEmpty(unittest.TestCase):

    def setUp(self):
        self.s_deque = Deque()

    def test_empty_size(self):
        self.assertEqual(self.s_deque.size(), 0)

    def test_empty_add_tail(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.add_tail(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[-1], new_item)

    def test_empty_add_front(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.add_front(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[0], new_item)

    def test_empty_remove_tail(self):
        len_queue = self.s_deque.size()
        self.assertEqual(self.s_deque.get_remove_tail_status(), 0)
        self.assertIsNone(self.s_deque.remove_tail())
        self.assertEqual(self.s_deque.get_remove_tail_status(), 2)
        self.assertEqual(self.s_deque.size(), len_queue)
        self.assertListEqual(self.s_deque.deque, [])

    def test_one_item_remove_front(self):
        len_queue = self.s_deque.size()
        self.assertEqual(self.s_deque.get_remove_front_status(), 0)
        self.assertIsNone(self.s_deque.remove_front())
        self.assertEqual(self.s_deque.get_remove_front_status(), 2)
        self.assertEqual(self.s_deque.size(), len_queue)
        self.assertListEqual(self.s_deque.deque, [])


class TestDequeManyItems(unittest.TestCase):

    def setUp(self):
        self.s_deque = Deque()
        number = random.randrange(3, 100)
        self.items_list = [random.randint(0, 100) for _ in range(number)]
        for item in self.items_list:
            self.s_deque.add_tail(item)

    def test_many_items_size(self):
        self.assertEqual(self.s_deque.size(), len(self.items_list))

    def test_many_items_add_tail(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.add_tail(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[-1], new_item)

    def test_many_items_add_front(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.add_front(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[0], new_item)

    def test_many_items_remove_tail(self):
        len_queue = self.s_deque.size()
        self.assertIsNone(self.s_deque.remove_tail())
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertListEqual(self.s_deque.deque, self.items_list[:-1])

    def test_many_items_remove_front(self):
        len_queue = self.s_deque.size()
        self.assertIsNone(self.s_deque.remove_front())
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertListEqual(self.s_deque.deque, self.items_list[1:])


if __name__ == '__main__':
    unittest.main()
