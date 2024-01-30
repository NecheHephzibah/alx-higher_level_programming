#!/usr/bin/python3

"""Defines a class Node that is part of a singly linked list"""


class Node:
    """Represents a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node.


        Args:
            data (int): Data inputs by user.
            next_node (struct): Pointer to the next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets and sets the data instance attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets and sets the pointer to the next_node instance"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize a singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Initialises the sorted lists, where the new node
           is inserted at the correct position in increasing
           order.


        Args:
            value (Node): the new node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Defines the print method for the singly linked list"""
        list_val = []
        temp = self.__head
        while temp is not None:
            list_val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(list_val))
