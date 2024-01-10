class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("Empty Circular Linked List")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Head)")

# Example usage:
if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list.append(5)
    circular_linked_list.append(10)
    circular_linked_list.append(15)
    
    print("Circular Linked List:")
    circular_linked_list.display()
