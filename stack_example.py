"""
This is the example file for Data structure - Stack
Chloe Huang
July, 2021
"""


# Create a Stack class and its methods
# We will first - Define the class
class Stack:

    # Constructor: This init method allows us to use a Python list 
    def __init__(self):
        self.items = list() #initialize an empty list


    # Use Push function to add an item to the stack 
    def push(self, item):
        self.items.append(item) # Use append to add the item 

    # Use the built in Pop method to remove items from the stack which automatically returns the last item of the list
    def pop(self):
        if self.items: # Give a condition: when there is item in the list, it will pop the last item, otherwise it will return None
            return self.items.pop()
        return None
    

    # We can peek what the next item is going to be removed
    def peek(self):
        if self.items: # Give a condition: when there is item in the list, it will peek the next item, otherwise it will return None
            return self.items[-1] 
        return None

    # Use size to know how many items are in the stack
    def size(self):
        return len(self.items)

    # Check if the stack is empty
    def is_empty(self):
        return self.items == []
    
    # To print out the stack
    def __str__(self):
        return str(self.items)

    




# Push
print("======Test 1 - Push =======")
new_stack = Stack()
new_stack.push('Money Stack')
new_stack.push('$5')
new_stack.push('$10')
print(new_stack) # expect output: ['Money Stack', '$5', '$10']
print("===========================")


print("======Test 2 - Pop =======")
new_stack.push('$20')
new_stack.push('$50')
new_stack.pop()
print(new_stack) # expect output: ['Money Stack', '$5', '$10', '$20']
print("==========================")

print("======Test 3 - Peek =======")
print(new_stack.peek()) # expect output: $20
print("==========================")


print("======Test 4 - Size =======")
print(new_stack.size()) # expect output: 4
print("==========================")


print("======Test 5 - Is empty =======")
print(new_stack.is_empty()) # expect output: FALSE
print("==========================")
