# Experiment 04: Circular Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CSLL:
    def __init__(self):
        self.start = None

    def insert_begin(self, data):
        new = Node(data)
        if self.start is None:
            self.start = new
            new.next = self.start
            return
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        new.next = self.start
        temp.next = new
        self.start = new

    def insert_end(self, data):
        new = Node(data)
        if self.start is None:
            self.start = new
            new.next = new
            return
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        temp.next = new
        new.next = self.start

    def insert_pos(self, pos, data):
        if pos == 1:
            self.insert_begin(data)
            return
        new = Node(data)
        temp = self.start
        for _ in range(pos - 2):
            if temp.next == self.start:
                break
            temp = temp.next
        new.next = temp.next
        temp.next = new

    def search(self, key):
        if self.start is None:
            print("List empty")
            return
        temp = self.start
        while True:
            if temp.data == key:
                print("Found:", key)
                return
            temp = temp.next
            if temp == self.start:
                break
        print("Not Found")

    def delete_begin(self):
        if self.start is None:
            print("Empty list")
            return
        temp = self.start
        while temp.next != self.start:
            temp = temp.next
        if self.start == temp:
            self.start = None
            return
        temp.next = self.start.next
        self.start = self.start.next

    def delete_end(self):
        if self.start is None:
            print("Empty list")
            return
        temp = self.start
        while temp.next.next != self.start:
            temp = temp.next
        temp.next = self.start

    def display(self):
        if self.start is None:
            print("List Empty")
            return
        temp = self.start
        while True:
            print(temp.data, end=" → ")
            temp = temp.next
            if temp == self.start:
                break
        print("(Back to Start)")

# Example:
# c = CSLL()
# c.insert_begin(10)
# c.display()
