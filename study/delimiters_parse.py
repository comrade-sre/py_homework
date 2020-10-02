#!/usr/bin/env python3
delimiters = [ i for i in input() if i in ["(",")", "[", "]", "{", "}"]]
brace_dict = {"(":")", "{":"}", "[":"]"}
def parse(delimiters: list):
    if  len(delimiters) % 2 != 0:
        print("there is an odd number of brackets in the input")
        exit(1)
    stack = []
    for i in delimiters:
        if i in ["(","{","["]:
           stack.append(i)
        if i in [")","}","]"] and i != brace_dict[stack.pop()]:
           print("there is disorder in brackets, current bracket without valid pair is", i)
           exit(2)
        if i in [")","}","]"] and len(stack) == 0:
           print("there is an empty stack with open brackets, current bracket without pair is", i)
           exit(3)     
               
                 
parse(delimiters)
