import os
import time
import util
import ctypes
import sys
import lock
import signal

from api import paper
from config.config import config
from config import path
from os import environ as env
from data import draw
from data import info

java: str = 'java'

__default_handler = None

def __handle_interrupt(num, frame):
  # Close everything
  lock.unlock()
  
  return __default_handler(num, frame)
  

def print_title() -> None:
  """Print executable information
  """
  print(draw.title)
  print(info.description)
  print('Made by', info.author)
  print('Version', info.version)
  print('======\n')

def _init() -> None:
  """Initialize executable data directories and start coroutines
  """
  if not os.path.isdir(path.local):
    os.makedirs(path.local)
  if not os.path.isdir(path.servers):
    os.makedirs(path.servers)

def install() -> None:
  """Install Java, Minecraft server and plugins...
  """
  print('Searching java...')
  
  if not util.have_java(): # Install Java
    print('Java not found, installing java...')
    if util.is_admin():
      p = util.install_java()
      print('Java installed at ' + p)
    else:
      t = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
      exit(1)
  else:
    print('Java found at', util.get_java_path())
    
  
  # Install Minecraft Server (TODO)

def init() -> None:
  lock.reserve_thread = lock.LockThread()
  lock.reserve_thread.deamon = True
  lock.reserve_thread.start()

def close() -> None:
  pass
  
def main() -> None:
  init()
  
  print_title()
  install()
  
  time.sleep(20)
  
  close()

def _start() -> None:
  _init()
  time_left = lock.lock()
  if not time_left: 
    main()
    lock.unlock()
    _ = input('Program complete, press Enter to exit...')
  else:
    print('Installer already running, exiting... (' + str(time_left) + ')')
    exit(1)
  

if __name__ == '__main__':
  __default_handler = signal.getsignal(signal.SIGINT)
  signal.signal(signal.SIGINT, __handle_interrupt)
  
  _start()
  
  