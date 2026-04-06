from collections import deque
def reversed_queue(q):
    stack=[]
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())

    return q
q=deque([1,2,3,4,5])
print("Original queue: ",list(q))
q1=reversed_queue(q)
print("The reversed queue is",list(q1))
