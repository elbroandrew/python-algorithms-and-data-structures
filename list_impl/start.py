from linked_list import *


def main():
    node1 = Node(2)
    node2 = Node(5)

    list1 = LinkedList(node1)
    list1.insert(node2)

    print(list1.node.next_node.value)


if __name__ == '__main__':
    main()
