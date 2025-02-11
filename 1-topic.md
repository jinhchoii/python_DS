<!--
What is the purpose of the data structure?

What is the performance of the data structure (you will need to talk about big O notation)?
What kind of problems can be solved using the data structure?

How would the data structure be used in Python (in some cases you will need to discuss recursion)?

What kind of errors are common when using the data structure? -->

# Table of Contents - Stack
Stack
* Introduction
* Stack of Money

Implementation
* Stack Methods
* Stack Performance

Prove
* Coding Challenge
* Resolution

Resources


# Stack
![MoneyStack](https://github.com/chloehuang18/Python-Data-Structure/blob/master/money-stack.PNG)

Figure 1 - Money Stack

A stack is a linear abstract data structure. When a new item is added to the stack, it is added from the the right or the top the of the list. It follows the principle of last-in-first-out(LIFO). The most recent item is the one to be removed.  
![Stack-1](https://github.com/chloehuang18/Python-Data-Structure/blob/master/stack_1.png)

Figure 2 - Stack Example
#
Let's look at an example diagram. 
#### 
![LIFO-1](https://github.com/chloehuang18/Python-Data-Structure/blob/master/stack_lifo.png)

Figure 3 - LIFO Principle

#
### Stack of money 
As figure 3 Lifo illustrates- Imagine that you were the cashier at walmart. When a customer came and give you a 5 dolloar bill to pay for a pack of gum, 
you open the cash register drawer and put that bill on the top of a stack of 5 dollor bills section. The next customer came, you add more bills on top of that stack. 
It would be a mess if you try to put or take a bill in the middle of the stack. The order in which you added the bill is preserved. 

# Implementation
Python build in data structure use a list as a stack. 

### 1. Push()
Push method is going to allow us to add an item onto the list. This function pass a parameter and appends it to the end of the stack.

Code:
```python
def push(self, item):
    self.items.append(item)  
```
Example:

![PushResult](https://github.com/chloehuang18/Python-Data-Structure/blob/master/push_result.PNG)

Figure 4 - Push Method

The performance for this method is O(1), becasue it uses append to add the item to the end of the list whcih happens in constant time. 
#
### 2. Pop()
Pop method is going to allow us to remove an item from the end of the stack.

Code:
```python
def pop(self):
# Give a condition: when there is item in the list, it will pop the last item, otherwise it will return None
    if self.items: 
    return self.items.pop()

    return None
    
```
Example:

![PopResult](https://github.com/chloehuang18/Python-Data-Structure/blob/master/pop_result.PNG)

Figure 5 - Pop Method

The performance for this method is also O(1), becasue it index the last item and remove it from the end of the stack whcih happens in constant time.
#
### 3. Peek()
Peek method returns the last item in the list.

Code:
```python
def peek(self):
# Give a condition: when there is item in the list, it will peek the next item, otherwise it will return None
    if self.items: 
        return self.items[-1] 
    return None    
```
Example:

![PeekResult](https://github.com/chloehuang18/Python-Data-Structure/blob/master/peek_result.png)

Figure 6 - Peek Method

The performance for this method is O(1), becasue it index the last item whcih happens in constant time.

#
### 4. Size()
Size method returns the length of the list that represents the stack.
We could also use len() to get the lenth of the list.

Code:
```python
def size(self):
        return len(self.items)
```
Example:

![SizeResult](https://github.com/chloehuang18/Python-Data-Structure/blob/master/size_result.png)

Figure 7 - Size Method

The performance for this method is O(1), becasue finding the length happens in constant time.

#
### 5. Is_empty()
Is_empty method returns a bollean value and check if the stack is empty.

Code:
```python
def is_empty(self):
    return self.items == []  
```
Example:

![EmptyResult](https://github.com/chloehuang18/Python-Data-Structure/blob/master/empty_result.png)

Figure 8 - Is emptys Method

The performance for this method is also O(1), becasue it index the last item and remove it from the end of the stack whcih happens in constant time.


# Performance

#

### Examples
[Example File](stack_example.py)

### Real life examples

1. Converting infix to postfix expressions.
2. Undo operation is also carried out through stacks.
3. Syntaxes in languages are parsed using stacks.
4. Forward – backward surfing in browser
5. History of visited websites
6. Message logs and all messages you get are arranged in stack
7. Call logs, E-mails, Google photos’ any gallery , YouTube downloads, Notifications ( latest appears first )

#
# Prove - Palindrome
Repeat sequences of DNA

The meaning of palindrome in the context of genetics is slightly different from the definition used for words and sentences. 
Since a double helix is formed by two paired antiparallel strands of nucleotides that run in opposite directions, 
and the nucleotides always pair in the same way 
(adenine (A) with thymine (T) in DNA or uracil (U) in RNA; cytosine (C) with guanine (G)), a (single-stranded)
nucleotide sequence is said to be a palindrome if it is equal to its reverse complement.

![dna](https://github.com/chloehuang18/Python-Data-Structure/blob/master/dna.png)

The challenge is to write a program that use stack to reverse the sequences of DNA.

If the sequences is GGATCC the palindrome sequences will be CCTAGG.

Download [Stack Challenge](stack_challenge.py)
#
### Resolution
Download [Stack Answer](stack_answer.py)
#
# Source
[Figure 1:Money-Stack](https://www.yourconroenews.com/business/bizfeed/article/Mississippi-bank-to-purchase-Houston-s-Icon-Bank-12847400.php)

[Figure 3: FILO](https://en.wikipedia.org/wiki/File:Lifo_stack.png)

[Palindromic sequence](https://en.wikipedia.org/wiki/Palindromic_sequence)
