"""
Suppose you have three nonempty stacks R, S, and T. Describe a sequence of operations that result in S
storing all elements originally in T bellow all of S's original elements, with both sets of those elementes
in their original order. The final configuration for R should be the same as its orginal configuration.
"""

import ArrayStack

r = ArrayStack.ArrayStack()

num = 1

for i in range(3):
    r.push(num)
    num += 1

num += 1
s = ArrayStack.ArrayStack()
for i in range(2):
    s.push(num)
    num += 1
num += 1

t = ArrayStack.ArrayStack()
for i in range(6):
    t.push(num)
    num += 1

r_pop = len(s) + len(t)

print("br:", r.p())
print("bs:", s.p())
print("bt:", t.p())

while not s.is_empty():
    r.push(s.pop())

while not t.is_empty():
    r.push(t.pop())

for i in range(r_pop):
    s.push(r.pop())

print('\n')
r.p()
s.p()
    
