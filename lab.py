#!/usr/bin/env python
def Queue():
    queue = Queue()
    queue.enqueue('4')
    queue.enqueue('3')
    queue.enqueue('2')
    n = queue.dequeue()
    m = queue.dequeue()
    l = queue.dequeue()
    queue.enqueue(m)
    queue.enqueue(l)
    queue.enqueue(m)
    l = queue.dequeue()
    while not queue.is_empty():
       return queue.dequeue(), end == ''