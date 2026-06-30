import time

def start_timer():
          return time.time()


def end_timer(start_time):
          end_time = time.time()
          total_time = end_time - start_time
          print("you finished in " + str(round(total_time)) + " Seconds!")