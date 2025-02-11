"""
This is the challenge file for Data structure - Stack
Chloe Huang
July, 2021
"""

"""
Repeat sequences of DNA

The meaning of palindrome in the context of genetics is slightly different from the definition used for words and sentences. 
Since a double helix is formed by two paired antiparallel strands of nucleotides that run in opposite directions, 
and the nucleotides always pair in the same way 
(adenine (A) with thymine (T) in DNA or uracil (U) in RNA; cytosine (C) with guanine (G)), a (single-stranded)
nucleotide sequence is said to be a palindrome if it is equal to its reverse complement.

The challenge is to write a program that use stack to reverse the sequences of DNA.

If the sequences is GGATCC the palindrome sequences will be CCTAGG.

"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items: 
            return self.items.pop()
        return None
    
    def is_empty(self):
        return self.items == []

"""
Problem 1
Use stack to write a function to find the palindrom of a given DNA sequence
"""
def palindrome_dna(stack, input_str):
    
    for i in range(len(input_str)):
        stack.push(input_str[i])

    reverse_dna = ""

    while not stack.is_empty():
        reverse_dna += stack.pop()

    return reverse_dna
    

"""
Problem 2
Use stack to write a function to check if a DNA sequences is palindrom
"""
def ispalindrome(stack, input_str):
    
    for i in input_str:
        stack2.push(i)
    
    reversed_dna = ""

    while not stack2.is_empty():
        reversed_dna = reversed_dna + stack2.pop()
    
    if input_str == reversed_dna:
        return True
    else:
        return False


print("======Test 1=======")
stack = Stack()
input_str = "GGATCC"
print(palindrome_dna(stack, input_str)) # expect output: CCTAGG

    
print("======Test 2=======")
stack2 = Stack()
input_str = "GAATTCCTTAAG"
print(ispalindrome(stack2, input_str)) # expect output: True
stack2 = Stack()
input_str = "TTGACCTTGACC"
print(ispalindrome(stack2, input_str)) # expect output: False
