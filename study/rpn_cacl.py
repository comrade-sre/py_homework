#!/usr/bin/env python3
stack = [i  for i in input() if i.isdigit() or i in ["-","+","*","/","//"]]
def calc(stack: list):
    operators = []
    res = 0
    while len(stack) > 0:
            i = stack.pop()
            if i in ["-","+","*","/","//"]:
               operators.append(i)
            if  i.isdigit() and  res == 0:
                second = i
                first = stack.pop()
                operator = operators.pop()
                res=eval(f'{first} {operator} {second}')
            elif i.isdigit() and  res != 0: 
                  operator = operators.pop()
                  res = eval(f'{res} {operator} {i}')
    print(res)
calc(stack)
