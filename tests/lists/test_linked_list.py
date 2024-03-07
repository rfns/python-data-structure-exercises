from unittest import TestCase

from algorithms.lists import LinkedList, Node


class TestLinkedList(TestCase):
    def test_linked_list_starts_with_zero_items(self):
        linked_list = LinkedList[int]()

        self.assertEqual(linked_list.get_size(), 0, "returns 0")

    def test_append_first_value_becomes_root_node(self):
        linked_list = LinkedList()

        linked_list.append_value(10)

        self.assertTrue(
            linked_list.root_node is not None
            and isinstance(linked_list.root_node, Node) is True
            and linked_list.root_node.get_value() == 10,
            "first value becomes root node",
        )

    def test_appended_second_value_becomes_tail_node_while_root_node_is_preserved(self):
        linked_list = LinkedList[int]()

        linked_list.append_value(10)
        linked_list.append_value(20)

        self.assertTrue(
            linked_list.tail_node is not None
            and isinstance(linked_list.tail_node, Node) is True
            and linked_list.tail_node.get_value() == 20
        )

        self.assertTrue(
            linked_list.root_node is not None
            and isinstance(linked_list.root_node, Node) is True
            and linked_list.root_node.get_value() == 10,
            "first value becomes root node",
        )

    def test_list_with_3_node_matches_ordering_through_iterator(self):
        linked_list = LinkedList[int]()

        linked_list.append_value(10)
        linked_list.append_value(20)
        linked_list.append_value(30)

        iterator = linked_list.get_iterator()
        iterator.next()
        self.assertEqual(iterator.get_value(), 10, "matches first node value")

        iterator.next()
        self.assertEqual(iterator.get_value(), 20, "matches second node value")

        iterator.next()
        self.assertEqual(iterator.get_value(), 30, "matches third value")

    def test_remove_first_node_should_shift_values_to_left(self):
        linked_list = LinkedList[int]()

        linked_list.append_value(10)
        linked_list.append_value(20)
        linked_list.append_value(30)

        linked_list.remove_at(0)

        iterator = linked_list.get_iterator()

        iterator.next()
        self.assertEqual(iterator.get_value(), 20, "matches second node value")

        iterator.next()
        self.assertEqual(iterator.get_value(), 30, "matches third value")

        self.assertTrue(
            iterator.next() is False and iterator.get_value() is None,
            "must have only two values",
        )

    def test_remove_last_node_should_not_shift_any_values(self):
        linked_list = LinkedList[int]()

        linked_list.append_value(10)
        linked_list.append_value(20)
        linked_list.append_value(30)

        linked_list.remove_at(2)

        iterator = linked_list.get_iterator()

        iterator.next()
        self.assertEqual(iterator.get_value(), 10, "matches second node value")

        iterator.next()
        self.assertEqual(iterator.get_value(), 20, "matches third value")

        self.assertTrue(
            iterator.next() is False and iterator.get_value() is None,
            "must have only two values",
        )

    def test_removing_middle_node_should_shift_values_from_the_right(self):
        linked_list = LinkedList[int]()

        linked_list.append_value(10)
        linked_list.append_value(20)
        linked_list.append_value(30)

        linked_list.remove_at(1)

        iterator = linked_list.get_iterator()

        iterator.next()
        self.assertEqual(iterator.get_value(), 10, "matches second node value")

        iterator.next()
        self.assertEqual(iterator.get_value(), 30, "matches third value")

        self.assertTrue(
            iterator.next() is False and iterator.get_value() is None,
            "must have only two values",
        )

    def test_insertion_at_end_has_the_same_result_than_append(self):
        linked_list = LinkedList[int]()
        maxed_out_index = 10

        linked_list.insert_at(maxed_out_index, 10)

        self.assertTrue(
            linked_list.tail_node is not None
            and isinstance(linked_list.tail_node, Node) is True
            and linked_list.tail_node.get_value() == 10
        )

    def test_insertion_at_beginning_shifts_existing_values_to_right(self):
        linked_list = LinkedList[str]()

        linked_list.append_value("10")
        linked_list.append_value("20")
        linked_list.append_value("30")

        expected_value = "Now I'm the first value!"

        linked_list.insert_at(0, expected_value)

        iterator = linked_list.get_iterator()

        iterator.next()
        self.assertEqual(iterator.get_value(), expected_value, "matches first value")

        iterator.next()
        self.assertEqual(iterator.get_value(), "10", "matches second node value")

        iterator.next()
        self.assertEqual(iterator.get_value(), "20", "matches third value")

        iterator.next()
        self.assertEqual(iterator.get_value(), "30", "matches third value")

        self.assertTrue(
            iterator.next() is False and iterator.get_value() is None,
            "must have only four values",
        )

    def test_insertion_middle_shifts_existing_afterwards_values_to_right(self):
        linked_list = LinkedList[str]()

        linked_list.append_value("10")
        linked_list.append_value("20")
        linked_list.append_value("30")

        expected_value = "I'm the new value I'm should be close to the middle!"

        linked_list.insert_at(2, expected_value)

        iterator = linked_list.get_iterator()

        iterator.next()
        self.assertEqual(iterator.get_value(), "10", "matches first node value")

        iterator.next()
        self.assertEqual(iterator.get_value(), "20", "matches second value")

        iterator.next()
        self.assertEqual(iterator.get_value(), expected_value, "matches third value")
        iterator.next()
        self.assertEqual(iterator.get_value(), "30", "matches fourth value")

        self.assertTrue(
            iterator.next() is False and iterator.get_value() is None,
            "must have only four values",
        )
