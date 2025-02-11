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
        #add your code here
        pass
    
    def pop(self):
        #add your code here
        pass
    
    def is_empty(self):
        return self.items == []
"""
Problem 1
Write a function that returns the palindrome DNA sequences of the given sequences
"""
def palindrome_dna(stack, input_str):
    #add your code here
    pass


"""
Problem 2
Write a function to check if a DNA sequences is palindrom
"""
def palindrome_checker(stack, input_str):
    #add your code here
    pass
    
    
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



