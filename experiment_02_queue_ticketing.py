# Experiment 02: Ticketing System Using Linear Queue

MAX = 5
queue = [None] * MAX
front = -1
rear = -1

def is_full():
    return rear == MAX - 1

def is_empty():
    return front == -1 or front > rear

def enqueue(ticket):
    global front, rear
    if is_full():
        print("Queue Overflow!")
        return
    if front == -1:
        front = 0
    rear += 1
    queue[rear] = ticket
    print(f"Ticket {ticket} added.")

def dequeue():
    global front
    if is_empty():
        print("Queue Underflow!")
        return
    print(f"Ticket {queue[front]} removed.")
    front += 1

def display():
    if is_empty():
        print("Queue is empty.")
    else:
        print("Queue:", queue[front:rear+1])

def size():
    if is_empty():
        return 0
    return rear - front + 1

def menu():
    while True:
        print("\n--- Ticketing Menu ---")
        print("1. Add Ticket\n2. Remove Ticket\n3. View Queue\n4. Size\n5. Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            t = input("Enter ticket no: ")
            enqueue(t)
        elif ch == 2:
            dequeue()
        elif ch == 3:
            display()
        elif ch == 4:
            print("Queue Size:", size())
        elif ch == 5:
            break
        else:
            print("Invalid choice!")

# menu()
