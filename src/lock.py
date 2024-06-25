import os
import time
import threading
from typing import Callable

from config import path

reserved_time:int = 5


__COUNTER_TIME: int = 1716999676

class LockThread(threading.Thread):
  """A Thread that keep the lock file active
  """
  def __init__(self, interval:float = 0.2) -> None:
    super(LockThread, self).__init__()
    self._stop_event = threading.Event()
    self.interval = interval
  
  def run(self) -> None:
        
    while not self._stop_event.is_set():
      if not _is_another_running():
        _serial_to_lock_file()
      else: 
        exit(1)
      time.sleep(self.interval)
    
  def stop(self) -> None:
    """Stop the thread at the next iteration
    """
    self._stop_event.set()
    
  def join(self, *args, **kwargs) -> None:
    """Stop and wait for the thread to syncrise it
    """
    self.stop()
    super(LockThread, self).join(*args, **kwargs)


reserve_thread: LockThread = None

def _serial_to_lock_file(t:int = reserved_time, pid:int = os.getpid(), file:str = path.lock_file) -> None:
  """Update the lock file to prevent duplicate installer instance

  Args:
      t (int, optional): The time to add to the file (time to reserve). Defaults to reserved_time.
      pid (int, optional): The pid of this instance. Defaults to os.getpid().
      file (str, optional): The file to write to. Defaults to path.lock_file.
  """
  t += int(time.time()) - __COUNTER_TIME
  with open(file, 'w') as f:
    f.write(';'.join((str(pid), str(t))))

def _parse_lock_file(file:str = path.lock_file) -> tuple[int, int]:
  """Get lock file information (pid and time left before release)

  Args:
      file (str, optional): File to read. Defaults to path.lock_file.

  Returns:
      tuple[int, int]: pid and time left for the reservation. -1 if problem reading the file (doesn't exist or problem)
  """
  pid, t = -1, -1
  
  try:
    with open(path.lock_file, 'r') as f:
      pid, t = (int(i) for i in f.read().split(';'))
  except:
    pass
  
  return pid, t - int(time.time()) + __COUNTER_TIME

def _is_another_running() -> int | None:
  """Check with the lock file if another instance of the installer is running

  Returns:
      int | None: Time left before release if locked
  """
  if os.path.isfile(path.lock_file):
    pid, time_left = _parse_lock_file()
    if pid > 0 and pid != os.getpid() and time_left > 0:
      return time_left
  return None

def lock() -> int | None:
  """Try to create the lock file

  Returns:
      int | None: Time left before release if file already exists
  """
  time_left = _is_another_running()
  if time_left:
    return time_left
  
  _serial_to_lock_file()
    
def unlock() -> None:
  """Free the lock file to let other installer run
  """
  if _is_another_running():
    return
  
  if reserve_thread:
    reserve_thread.join()
  
  if os.path.isfile(path.lock_file):
    os.remove(path.lock_file)
    
def run_thread_locker() -> None:
  """Run the thread to update the lock_file while the installer is running. To prevent infinite locking in case of a crash
  """
  reserve_thread = LockThread()
  reserve_thread.deamon = True
  reserve_thread.start()
