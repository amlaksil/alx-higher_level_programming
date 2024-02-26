#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    """Node class that defines singly linked list.

    Attributes:
        data: The data stored in the node.
        next_node: A reference to the next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """Initializing the node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter to retrieve the data """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""singly linked list module """


class SinglyLinkedList:
    """Defines singly linked list.
    Attributes:
        __head: The head node of the linked list.
    """
    def __init__(self):
        """Initializes the linked list."""
        self.__head = None

    def __str__(self):
        """
        Returns a sring representation of the linked list.

        Returns:
            A string representing the linked lits, with each element separated
            by a newline character.
        """
        head = self.__head
        data = []
        while head is not None:
            data.append(head.data)
            head = head.next_node
        fstr = ''
        new_line = '\n'
        for i in range(0, len(data)):
            if i == len(data) - 1:
                new_line = ''
            fstr += f'{data[i]}{new_line}'
        return fstr

    def sorted_insert(self, value):
        """
        Inserts a value into the linked list in a sorted manner.

        Args:
            value: The value to be inserted into the linked list.
        """
        new_node = Node(value)
        ptr = prev = self.__head
        if ptr is None:
            self.__head = new_node
            return
        if new_node.data <= ptr.data:
            new_node.next_node = ptr
            self.__head = new_node
            return

        while ptr is not None:
            if ptr.next_node is None and new_node.data >= ptr.data:
                ptr.next_node = new_node
                break
            elif new_node.data <= ptr.data:
                new_node.next_node = ptr
                prev.next_node = new_node
                break
            prev = ptr
            ptr = ptr.next_node
        return
