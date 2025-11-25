# Experiment 03: Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.start = None

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.start
        self.start = new

    def insert_end(self, data):
        new = Node(data)
        if self.start is None:
            self.start = new
            return
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = new

    def insert_pos(self, pos, data):
        if pos == 1:
            self.insert_begin(data)
            return
        new = Node(data)
        temp = self.start
        for _ in range(pos - 2):
            if temp is None:
                break
            temp = temp.next
        if temp is None:
            self.insert_end(data)
        else:
            new.next = temp.next
            temp.next = new

    def delete_begin(self):
        if self.start is None:
            print("List empty")
            return
        self.start = self.start.next

    def delete_end(self):
        if self.start is None:
            print("Empty list")
            return
        if self.start.next is None:
            self.start = None
            return
        temp = self.start
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search(self, key):
        temp = self.start
        while temp:
            if temp.data == key:
                print("Found:", key)
                return
            temp = temp.next
        print("Not Found")

    def display(self):
        temp = self.start
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

# Example:
# s = SLL()
# s.insert_begin(10)
# s.display()
