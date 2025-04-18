# create a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
# Insert at the beginning
    def insertAtBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
# Deleting a node
    def delete_beginning(self):
        if self.head is None:
            print("ll is empty")
        else:
            self.head=self.head.next
# Print the ll
    def printlist(self):
        temp=self.head
    while(temp):
        print(temp.data)
        temp=temp.next
# Creating LinkedList and adding nodes
llist = ll()
n=Node(1)
llist.head=n
n1=Node(2)
n.next=n1
# Inserting at the beginning
llist.insertAtBeginning(10)
llist.insertAtBeginning(20)
llist.insertAtBeginning(30)
# Printing the ll.
print("ll")
llist.printlist()
# Delegting a node at the beginning
print("after deleting")
llist.delete_beginning()
llist.printlist()



