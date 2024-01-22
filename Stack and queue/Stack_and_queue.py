class Node:
    def __init__(self, message):
        self.message = message
        self.next = None


# Function to add a message to the stack
def push(top, message):
    new_node = Node(message)
    new_node.next = top
    return new_node


# Function to remove a message from the stack
def pop(top):
    if top is None:
        print("Stack is empty!")
        return None, None
    temp = top
    top = top.next
    return top, temp.message


# Function to add a message to the queue
def enqueue(front, rear, message):
    new_node = Node(message)
    if rear is None:
        front = rear = new_node
        return front, rear
    rear.next = new_node
    rear = new_node
    return front, rear


# Function to remove a message from the queue
def dequeue(front, rear):
    if front is None:
        print("Queue is empty!")
        return None, None, None
    temp = front
    front = front.next
    if front is None:
        rear = None
    return front, rear, temp.message


# Function to display messages from a stack or queue
def display(head):
    while head is not None:
        print(head.message)
        head = head.next


# Additional function to display conversation
def display_conversation(stack, queue):
    # Convert stack to queue to maintain order
    temp_stack = None
    while stack is not None:
        stack, message = pop(stack)
        temp_stack = push(temp_stack, message)

    # Alternate messages from temp_stack and queue
    while temp_stack is not None or queue is not None:
        if temp_stack is not None:
            temp_stack, message = pop(temp_stack)
            print(message)

        if queue is not None:
            queue, _, message = dequeue(queue, None)
            print(message)


# Main function
if __name__ == "__main__":
    stack_top = None
    queue_front = None
    queue_rear = None

    # Example fictional conversation messages
    # Adding messages to the stack and queue
    stack_top = push(stack_top, "Eric: Hey, what's up?")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Not much, just chilling.")
    stack_top = push(stack_top, "Eric: Doing some coding, you?")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Oh cool, what are you coding?")
    stack_top = push(stack_top, "Eric: Just working on a small project for class.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Nice! I'm just watching some TV.")
    stack_top = push(stack_top, "Eric: Anything interesting?")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Yeah, watching 'The 100'. Ever seen it?")
    stack_top = push(stack_top, "Eric: Heard of it, never got around to watching it though.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: It's pretty good, you should check it out.")
    stack_top = push(stack_top, "Eric: Maybe I will. Need a break from coding anyway.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Definitely, let's catch up later?")
    stack_top = push(stack_top, "Eric: Sounds good, talk to you later!")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Later!")
    stack_top = push(stack_top, "Eric: Doing some coding, you?")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Oh cool, what are you coding?")
    stack_top = push(stack_top, "Eric: Just working on a small project for class.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Nice! I'm just watching some TV.")
    stack_top = push(stack_top, "Eric: Anything interesting?")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Yeah, watching 'The 100'. Ever seen it?")
    stack_top = push(stack_top, "Eric: Heard of it, never got around to watching it though.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: It's pretty good, you should check it out.")
    stack_top = push(stack_top, "Eric: Maybe I will. Need a break from coding anyway.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Definitely, let's catch up later?")
    stack_top = push(stack_top, "Eric: Sounds good, talk to you later!")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Later!")
    stack_top = push(stack_top, "Eric: Hey, wait, is the stuff up yet?")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Not much, just hanging out at home.")
    stack_top = push(stack_top, "Eric: Same here, bored out of my mind.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Want to come over and watch a movie or something?")
    stack_top = push(stack_top, "Eric: Sure, that sounds like a good idea.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Great, I'll see you in about 30 minutes.")
    stack_top = push(stack_top, "Eric: Sounds good, see you soon.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Do you have any movie preferences?")
    stack_top = push(stack_top, "Eric: Not really, anything you want to watch is fine with me.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: How about a comedy? I could use a good laugh.")
    stack_top = push(stack_top, "Eric: That works for me.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Okay, I'm on my way.")
    stack_top = push(stack_top, "Eric: Alright, I'll see you soon.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Sorry, I'm running a bit late. Be there in 10 minutes.")
    stack_top = push(stack_top, "Eric: No worries, take your time.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Okay, I'm here.")
    stack_top = push(stack_top, "Eric: I'll be right down.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: Sounds good.")
    stack_top = push(stack_top, "Eric: That was a hilarious movie.")
    queue_front, queue_rear = enqueue(queue_front, queue_rear, "Amoh: I'm glad you liked it.")
    # ...the messages can continue....

    # Menu choices
    while True:
        print("\nWELCOME TO Python Stack and Queue\n \nA sequence of messages demonstrating a back-and-forth conversation \nbetween two people (Person_1: Eric & Person_2: Amoh)\n")
        print("Choose an option:\n")
        print("1. Display Eric's stack")
        print("2. Display Amoh's queue")
        print("3. Display the conversation")
        print("4. Exit")

        choice = int(input())

        if choice == 1:
            print("Eric's Stack messages:")
            display(stack_top)
        elif choice == 2:
            print("Amoh's Queue messages:")
            display(queue_front)
        elif choice == 3:
            print("Conversation:")
            display_conversation(stack_top, queue_front)
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

