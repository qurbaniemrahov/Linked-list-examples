class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None        

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev=self.tail
            self.tail.next = new_node
            self.tail=new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data,end="<->")
            current=current.next
        print("None")      

    def display_backward(self):
        current=self.tail
        while current:
            print(current.data,end="<->")
            current = current.prev
        print("None")     
if __name__== "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(5)
    doubly_linked_list.append(10)
    doubly_linked_list.append(15)

    print("Doubly Linked List (Forward):")
    doubly_linked_list.display_forward()

    print("\nDoubly Linked List (Backward):")
    doubly_linked_list.display_backward()


    