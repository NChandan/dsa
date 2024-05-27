class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        current =self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element: Node, position: int):
        count = 1
        if count == position:
            new_element.next = self.head.next
            self.head = new_element
        else:
            current = self.head
            while current:
                if position == count+1:
                    new_element.next = current.next
                    current.next = new_element
                    return
                else:
                    count += 1
                    current = current.next

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    an4 = Node(4)

    in5 = Node(3)

    ll = LinkedList()
    ll.append(n1)
    ll.append(n2)
    ll.append(n3)
    ll.print()
    ll.insert(in5, 3)
    ll.insert(an4, 1)
    ll.print()