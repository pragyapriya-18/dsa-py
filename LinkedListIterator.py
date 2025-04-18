class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if (self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node


    # Generator function to iterate through the list
    def print_iter(self):
        current_item = self.head
        while current_item:
            val =  current_item.data
            current_item = current_item.next
            yield val

# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

for i in ll.print_iter():
    print(i)