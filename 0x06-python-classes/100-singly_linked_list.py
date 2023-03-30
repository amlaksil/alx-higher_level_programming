#!/usr/bin/python3
"""Singly linked list module"""


class Node:
    """Node class that defines singly linked list"""
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
        sel.__next_node = value


"""singly linked list module """


class SinglyLinkedList:
    """defines singly linked list """
    def __str__(self):
        """Initializing singly linked list """
        rtn = ""
        ptr = self.__head

        while prt is not None:
            rtn += str(ptr.data)
            if prt.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

            return rtn

    def __init__(self):
        """Initialize the node """
        self.__head = None

    def sorted_insert(self, value):
        """sort the list """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

            newNode = Node(value, ptr)
            if ptr == self.__head:
                self.__head = newNode
            else:
                ptr_prev.next_node = newNode
