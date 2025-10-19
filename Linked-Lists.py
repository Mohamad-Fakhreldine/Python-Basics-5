class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show_list(self):
        current = self.head
        if current is None:
            print("The list is empty")
            return
        else:
            while current != None:
                print(current.data)
                print("||")
                current = current.next
    
    def add_start(self):
        node_data = input("Enter the value of the first node: ")
        new_node = Node(node_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def add_end(self):
        node_data = input("Enter the value of the last node: ")
        new_node = Node(node_data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    
    def insert(self):
        target = input("Enter an existing node: ")
        node_data = input("Enter the value of the node to be inserted after the chosen node: ")
        new_node = Node(node_data)
        if self.head is None:
            print("The list is empty.")
            return
        else:
            current = self.head
            while current.next != None:
                if current.data == target:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next

prompt = """
1. Show current list.
2. Add a new node at the beginning of the list.
3. Add a new node at the end of the list.
4. Insert a new node after the node containing a given value.
5. Delete the first occurrence of a node containing the given value.
6. Return True if a node with the given value exists, otherwise False.
7. Return the total number of nodes in the list.
8. Reverse the list in-place, so that the first node becomes the last.
9. Print the full list in a readable way, showing the links between nodes.
10. Return True if the list is empty, else False.
11. Clear the list.
12. Display the middle node's data.
13. Convert the linked list to a regular Python list.
14. Exit.
"""
l = LinkedList()

while True:
    print(prompt)
    choice = input("Choose an option: ")
    if choice == "1":
        l.show_list()
    elif choice == "2":
        l.add_start()
    elif choice == "3":
        l.add_end()
    elif choice == "4":
        l.insert()
    elif choice == "14":
        exit()
    else: 
        print("Invalid choice.")