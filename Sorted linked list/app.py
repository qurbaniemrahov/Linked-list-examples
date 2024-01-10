class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head or data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    sorted_linked_list = SortedLinkedList()
    sorted_linked_list.insert(10)
    sorted_linked_list.insert(5)
    sorted_linked_list.insert(20)
    sorted_linked_list.insert(3)
    
    print("Sorted Linked List:")
    sorted_linked_list.display()
