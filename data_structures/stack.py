# Basics of a Stack:
# LIFO (last in, first out)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()

    print("Testing is_empty functionality:")
    print(s.is_empty(), "\n")

    print("Pushing the values 5, 6, and 7:")
    s.push(5)
    s.push(6)
    s.push(7)
    print(s, "\n")

    print("Removing the last value added in the stack:")
    s.pop()
    print(s, "\n")

    print("Looking at the top of the stack:")
    print(s.peek(), "\n")

    print("Checking the size of the stack:")
    print(s.size(), "\n")

    # Reversing a string example
    print("Testing algorithm to reverse a string")
    reversed_string = ""
    user_input = input("Enter a string to reverse:")

    initial = Stack()

    for character in user_input:
        initial.push(character)

    while initial.is_empty() != True:
        reversed_string = reversed_string + initial.pop()
    print(reversed_string)
