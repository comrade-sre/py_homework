#!/usr/bin/env python3
import timeit
import random
m = random.randint(500,10000)
quotes_raw = [ x**3 for x in range(10,m,3) ] 
quotes = random.sample(quotes_raw, len(quotes_raw))

def isStackEmpty(s):
    if len(s) > 0:
        return False
    else:
        return True

def span_calc(quotes):
   spans = []
   for i in range(len(quotes)):
       k = 1
       span_end = False
       while not span_end and i - k >= 0: 
           if quotes[i - k] <= quotes[i]:
              k = k + 1
           else:
              span_end = True
       spans.append(k)
   return spans

def span_stack_calc(quotes):
    spans = []
    s = []
    spans.insert(0, 1)
    s.append(0)
    for i in range(1, len(quotes)):
        while not isStackEmpty(s) and quotes[s[len(s) - 1]] <= quotes[i]:
              s.pop()
        if isStackEmpty(s):
           spans.insert(i, i + 1)
        else:
           spans.insert(i, i - s[len(s) - 1])
        s.append(i)
    return spans

print(quotes)
print(span_calc(quotes))
print(span_stack_calc(quotes))
print("execution time without a stack is", timeit.timeit("span_calc(quotes)", number=10, globals=globals()))
print("execution time with a stack is", timeit.timeit("span_stack_calc(quotes)", number=10, globals=globals()))
