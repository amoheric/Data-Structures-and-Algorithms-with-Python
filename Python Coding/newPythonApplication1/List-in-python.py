# NAME: ERIC AMOH ADJEI
# DATE: 01/14/2024
# ASSIGNMENT 1: LIST 
#
#

# Define a Node class to represent individual items in the linked list
class Node:
    def __init__(self, url):
        self.url = url  # Initializing the Node with a URL
        self.next = None  # Initializes the reference to the next Node as None
        self.prev = None  # Initializes the reference to the previous Node as None
        

# Defines a LinkedList class to manage a list of Nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Initializes the head of the linked list as None
        self.tail = None  # Initializes the tail of the linked list as None
        self.current = None  # Initializes a current node to keep track of the current position in the list
        

    def append(self, url):
        
        # Creates a new Node with the given URL
        new_node = Node(url)
        
        
        if not self.head:
            
            # If the linked list is empty, set the new Node as both the head and tail
            self.head = new_node
            self.tail = new_node
            self.current = new_node
            
        else:
            # If the linked list is not empty, update the references to insert the new Node at the end
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            

    def display(self):
        current = self.head
        
        while current:
            
            # Traverses the linked list and print the URL of each Node
            print(current.url)
            current = current.next

    def go_forward(self):
        if self.current.next:
            
            # Moves the current position forward and print the URL of the new current Node
            self.current = self.current.next
            print("Forward: ", self.current.url)
            
        else:
            # Notifies when the end of the list is reached
            print("End of the list reached.")

    def go_backward(self):
        if self.current.prev:
            
            # Moves the current position backward and print the URL of the new current Node
            self.current = self.current.prev
            print("Backward: ", self.current.url)
            
        else:
            
            # Notifies when the beginning of the list is reached
            print("Beginning of the list reached.")

    def delete(self, url):
        current = self.head
        while current:
            
            if current.url == url:
                
                # Finds the Node with the specified URL and remove it from the list
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                print("Deleted: ", url)
                return
            current = current.next
        # Notify when the URL is not found in the list
        print("URL not found in the list.")

    def search(self, url):
        current = self.head
        while current:
            if current.url == url:
                # Finds the Node with the specified URL and print a message when found
                print("Found: ", url)
                return
            current = current.next
        # Notify when the URL is not found in the list
        print("URL not found in the list.")


# Defining the main part of the program
if __name__ == "__main__":
    
    # A Welcome message and introduction
    print("Welcome to the Website Manager App!")
    print("This app allows you to manage a list of websites.")
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    print(f"Hi {name}, you are {age} years old.")
    print("Here are the available functions of the app:")
    


    # Creating a linked list and add a list of websites to it
    linked_list = LinkedList()
    
    # Adding the list of websites
    websites = [
        "http://amoheric.com",
        "http://jw.org",
        "http://google.org",
        "http://microsoft.org",
        "http://bing.org",
        "http://jw2.org",
        "http://jw3.org",
        "http://jw4.org",
        "http://jw5.org",
        "http://jw6.org",
        "http://jw7.org",
        "http://jw8.org",
        "http://canva.com",
        "http://pinterest.com",
        "http://credstat.net",
        "http://jw9.org",
        "http://jw0.org",
        "http://jw1.org",
        "http://123movies.com",
        "http://homedepot.com",
    ]
    for website in websites:
        linked_list.append(website)
        

# Creating a menu interface for the user to interact with the linked list
    while True:
        print("\nMenu:")
        print("1. Display the list")
        print("2. Go forward and display the webpage")
        print("3. Go backward and display the webpage")
        print("4. Add another item to the list")
        print("5. Delete an item from the list")
        print("6. Find an item in the list")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            linked_list.display()
        elif choice == '2':
            linked_list.go_forward()
        elif choice == '3':
            linked_list.go_backward()
        elif choice == '4':
            url = input("Enter the URL to add: ")
            linked_list.append(url)
        elif choice == '5':
            url = input("Enter the URL to delete: ")
            linked_list.delete(url)
        elif choice == '6':
            url = input("Enter the URL to search: ")
            linked_list.search(url)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Menu interface
def menu():
    linked_list = LinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Display the list")
        print("2. Go forward and display the webpage")
        print("3. Go backward and display the webpage")
        print("4. Add another item to the list")
        print("5. Delete an item from the list")
        print("6. Find an item in the list")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            linked_list.display()
        elif choice == '2':
            linked_list.go_forward()
        elif choice == '3':
            linked_list.go_backward()
        elif choice == '4':
            url = input("Enter the URL to add: ")
            linked_list.append(url)
        elif choice == '5':
            url = input("Enter the URL to delete: ")
            linked_list.delete(url)
        elif choice == '6':
            url = input("Enter the URL to search: ")
            linked_list.search(url)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

