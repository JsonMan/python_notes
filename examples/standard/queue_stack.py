'''
Created on 2013-9-4

@author: Administrator
'''
import Queue

Empty = Queue.Empty

class Stack(Queue.Queue):
    "thread-safe stack"
    
    def __put__(self, item):
        self.queue.insert(0, item)
    
    push = Queue.Queue.put
    pop = Queue.Queue.get 
    pop_nowait = Queue.Queue.get_nowait


stack = Stack(0)
stack.push("first")
stack.push("second")
stack.push("third")

try:
    while 1:
        print stack.pop_nowait()
except Empty:
    pass


