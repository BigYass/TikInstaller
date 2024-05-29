import os
import time
import threading
from typing import Callable

from config import path

reserved_time:int = 5


__COUNTER_TIME: int = 1716999676

class LockThread(threading.Thread):
  def __init__(self, interval:float = 0.2) -> None:
    super(LockThread, self).__init__()
    self._stop_event = threading.Event()
    self.interval = interval
  
  def run(self) -> None:
        
    while not self._stop_event.is_set():
      if not _is_another_running():
        _serial_to_lock_file()
      else:
        print('Another running, stoping')
        exit(1)
      time.sleep(self.interval)
    
  def stop(self) -> None:
    self._stop_event.set()
    
  def join(self, *args, **kwargs) -> None:
    self.stop()
    super(LockThread, self).join(*args, **kwargs)

reserve_thread: LockThread = None

def _serial_to_lock_file(t:int = reserved_time, pid:int = os.getpid(), file:str = path.lock_file) -> None:
  t += int(time.time()) - __COUNTER_TIME
  with open(file, 'w') as f:
    f.write(';'.join((str(pid), str(t))))

def _parse_lock_file(file:str = path.lock_file) -> tuple[int, int]:
  pid, t = -1, -1
  
  try:
    with open(path.lock_file, 'r') as f:
      pid, t = (int(i) for i in f.read().split(';'))
  except:
    pass
  
  return pid, t - int(time.time()) + __COUNTER_TIME

def _is_another_running() -> int | None:
  if os.path.isfile(path.lock_file):
    pid, time_left = _parse_lock_file()
    if pid > 0 and pid != os.getpid() and time_left > 0:
      return time_left
  return None

def lock() -> int | None:
  time_left = _is_another_running()
  if time_left:
    return time_left
  
  _serial_to_lock_file()
    
def unlock() -> None:  
  if _is_another_running():
    return
  
  if reserve_thread:
    reserve_thread.join()
  
  if os.path.isfile(path.lock_file):
    os.remove(path.lock_file)
    
    
