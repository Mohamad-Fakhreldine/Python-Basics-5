class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


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

while True:
    print(prompt)
    choice = input("Choose an option: ")
    if choice == "1":
        print("Not implemented yet")
    elif choice == "14":
        exit()
    else: 
        print("Invalid choice.")
