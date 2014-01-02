'''
Created on 2013-9-4

@author: Administrator
'''

import Queue
import bisect

Empty = Queue.Empty

class PriorityQueue(Queue.Queue):
    "thread-safe priority queue"
    
    def __put(self, item):
        bisect.insort(self.queue, item)

queue = PriorityQueue(0)
queue.put(20)
queue.put(10)
queue.put(30)
queue.put(3)
queue.put(300)

try:
    while 1:
        print queue.get_nowait()
except Empty:
    pass 


