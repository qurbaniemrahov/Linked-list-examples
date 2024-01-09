class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")         
if __name__=="__main__":
    linked_list=linkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.display()    