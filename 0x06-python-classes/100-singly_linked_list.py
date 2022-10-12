#!/usr/bin/python3

class Node:
    """ defines a node of singly linked list """

    def __init__(self, data, next_node=None):
        """ initializes the node

            Args:
                data (int): number inside a node
                node (node): a node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter """

        return self.__data

    @data.setter
    def data(self, value):
        """ data setter """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ next_node getter """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next_node setter """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list class """
    def __init__(self):
        """ initializes a singly linked list node """

        self.__head = None

    def sorted_insert(self, value):
        """ inserts new Node into a singly linked list

            the new node is inserted into the correct sorted
            postion (increasing order)

            Args:
                value (node): The node to be inserted
        """

        new = Node(value)
        if self.__head is None:
            self.__head = new
            self.__head.next = None
            return
        if self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node is not None:
                if temp.next_node.data < value:
                    temp = temp.next_node
                else:
                    break
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """ defines print() value of SinglyLinkedList """

        temp = self.__head
        while temp.next_node is not None:
            print(str(temp.data))
            temp = temp.next_node
        return (str(temp.data))
