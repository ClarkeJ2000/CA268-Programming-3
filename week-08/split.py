from Queue import Queue

def split(q):
   q1 = Queue()
   q2 = Queue()
   for i in range(len(q)):
      if i % 2:
          q1.enqueue(q.dequeue())
      else:
          q2.enqueue(q.dequeue())
  
  return q1, q2