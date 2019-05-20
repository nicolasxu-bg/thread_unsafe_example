import threading

x = 0

class Counter():
   def __init__(self):
      self.counter = 0

nick_counter = Counter()

def increment_global():

   global nick_counter
   nick_counter.counter += 1

def taskofThread(lock):

   for _ in range(50000):
      # with lock:
      increment_global()

def main():
   global x
   x = 0

   lock = threading.Lock()
   t1 = threading.Thread(target = taskofThread, args = (lock,))
   t2 = threading.Thread(target = taskofThread, args = (lock,))

   t1.start()
   t2.start()

   t1.join()
   t2.join()

if __name__ == "__main__":
   for i in range(5):
      main()
      print("x = {1} after Iteration {0}".format(i, nick_counter.counter))

# result with lock
# x = 100000 after Iteration 0
# x = 200000 after Iteration 1
# x = 300000 after Iteration 2
# x = 400000 after Iteration 3
# x = 500000 after Iteration 4

# result without lock
# x = 81809 after Iteration 0
# x = 164319 after Iteration 1
# x = 247065 after Iteration 2
# x = 330986 after Iteration 3
# x = 413088 after Iteration 4
