import random
import unittest

from BoundedStack import BoundedStack


class TestBoundedStackOneItem(unittest.TestCase):

    def setUp(self):
        self.s_stack = BoundedStack()
        self.number = random.randint(0, 100)
        self.s_stack.push(self.number)

    def test_one_item_size(self):
        self.assertEqual(self.s_stack.size(), 1)

    def test_one_item_push(self):
        len_stack = self.s_stack.size()
        new_item = random.randint(0, 100)
        self.assertEqual(self.s_stack.get_push_status(), 1)
        self.assertIsNone(self.s_stack.push(new_item))
        self.assertEqual(self.s_stack.get_push_status(), 1)
        self.assertEqual(self.s_stack.size(), len_stack + 1)
        self.assertEqual(self.s_stack._items[-1], new_item)

    def test_one_item_pop(self):
        len_stack = self.s_stack.size()
        self.assertEqual(self.s_stack.get_pop_status(), 0)
        self.assertIsNone(self.s_stack.pop())
        self.assertEqual(self.s_stack.get_pop_status(), 1)
        self.assertEqual(self.s_stack.size(), len_stack - 1)
        self.assertEqual(self.s_stack._items, [])

    def test_one_item_peek(self):
        len_stack = self.s_stack.size()
        self.assertEqual(self.s_stack.get_peek_status(), 0)
        self.assertEqual(self.s_stack.peek(), self.s_stack._items[-1])
        self.assertEqual(self.s_stack.get_peek_status(), 1)
        self.assertEqual(self.s_stack.size(), len_stack)
        self.assertEqual(self.s_stack._items, [self.number])


class TestBoundedStackEmpty(unittest.TestCase):

    def setUp(self):
        self.s_stack = BoundedStack()

    def test_empty_size(self):
        self.assertEqual(self.s_stack.size(), 0)

    def test_empty_push(self):
        len_stack = self.s_stack.size()
        new_item = random.randint(0, 100)
        self.assertEqual(self.s_stack.get_push_status(), 0)
        self.assertIsNone(self.s_stack.push(new_item))
        self.assertEqual(self.s_stack.get_push_status(), 1)
        self.assertEqual(self.s_stack.size(), len_stack + 1)
        self.assertEqual(self.s_stack._items[-1], new_item)

    def test_empty_pop(self):
        len_stack = self.s_stack.size()
        self.assertEqual(self.s_stack.get_pop_status(), 0)
        self.assertIsNone(self.s_stack.pop())
        self.assertEqual(self.s_stack.get_pop_status(), 2)
        self.assertEqual(self.s_stack.size(), len_stack)
        self.assertEqual(self.s_stack._items, [])

    def test_empty_peek(self):
        len_stack = self.s_stack.size()
        self.assertEqual(self.s_stack.get_peek_status(), 0)
        self.assertIsNone(self.s_stack.peek())
        self.assertEqual(self.s_stack.get_peek_status(), 2)
        self.assertEqual(self.s_stack.size(), len_stack)
        self.assertEqual(self.s_stack._items, [])


class TestBoundedStackFull(unittest.TestCase):

    def setUp(self):
        self.s_stack = BoundedStack()
        number = 32
        self.items_list = [random.randint(0, 100) for _ in range(number)]
        for item in self.items_list:
            self.s_stack.push(item)

    def test_many_items_size(self):
        self.assertEqual(self.s_stack.size(), len(self.items_list))

    def test_many_items_push(self):
        new_item = 1000
        self.assertEqual(self.s_stack.get_push_status(), 1)
        self.assertIsNone(self.s_stack.push(new_item))
        self.assertEqual(self.s_stack.get_push_status(), 2)
        self.assertEqual(self.s_stack.size(), len(self.items_list))
        self.assertListEqual(self.s_stack._items, self.items_list)

    def test_many_items_pop(self):
        self.assertEqual(self.s_stack.get_pop_status(), 0)
        self.assertIsNone(self.s_stack.pop())
        self.assertEqual(self.s_stack.get_pop_status(), 1)
        self.assertEqual(self.s_stack.size(), len(self.items_list) - 1)
        self.assertListEqual(self.s_stack._items, self.items_list[:-1])
        self.assertEqual(self.s_stack.get_pop_status(), 1)
        self.assertIsNone(self.s_stack.pop())
        self.assertEqual(self.s_stack.get_pop_status(), 1)
        self.assertEqual(self.s_stack.size(), len(self.items_list) - 2)
        self.assertListEqual(self.s_stack._items, self.items_list[:-2])

    def test_many_items_peek(self):
        self.assertEqual(self.s_stack.get_peek_status(), 0)
        self.assertEqual(self.s_stack.peek(), self.items_list[-1])
        self.assertEqual(self.s_stack.get_peek_status(), 1)
        self.assertEqual(self.s_stack.size(), len(self.items_list))
        self.assertListEqual(self.s_stack._items, self.items_list)
        self.assertEqual(self.s_stack.get_peek_status(), 1)
        self.assertEqual(self.s_stack.peek(), self.items_list[-1])
        self.assertEqual(self.s_stack.get_peek_status(), 1)
        self.assertEqual(self.s_stack.size(), len(self.items_list))
        self.assertListEqual(self.s_stack._items, self.items_list)


if __name__ == '__main__':
    unittest.main()
