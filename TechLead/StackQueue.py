from collections import deque
s = [1,3,5,7]
d = deque([2,4,6,8,10])
d.append(12)
print(d)
print(d.popleft())
print(d)