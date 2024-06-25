import os
import time
import ctypes
import sys
import lock
import signal

from api import paper
from util import java
from util import util
from config.config import Config
from config import path
from os import environ as env
from data import draw
from data import info
from data.text import lang, KEYS 

__default_handler = None

def __handle_interrupt(num, frame):
  # Close everything
  lock.unlock()
  
  return __default_handler(num, frame)
  

def print_title() -> None:
  """Print executable information
  """
  print(draw.title)
  print(lang[KEYS.EXE_DESCRIPTION])
  print(lang[KEYS.EXE_MADE_BY].format(info.author))
  print(lang[KEYS.EXE_VERSION].format(info.version))
  print('======\n')

def _init() -> None:
  """Initialize executable data directories and start coroutines
  """
  if not os.path.isdir(path.local):
    os.makedirs(path.local)
  if not os.path.isdir(path.servers):
    os.makedirs(path.servers)

def install_java() -> None:
  # Check java and Install it
  print(lang[KEYS.LOG_INS_JAVA_SEARCHING])
  
  if not java.have_java(): # Install Java
    print(lang[KEYS.LOG_INS_JAVA_NOT_FOUND])
    if util.is_admin():
      p = java.install_java(Config.java_version)
      print(lang[KEYS.LOG_INS_JAVA_INSTALLED].format(p))
    else:
      t = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
      close(0)
  else:
    print(lang[KEYS.LOG_INS_JAVA_FOUND].format(java.get_java_path()))
    
def install_server() -> None:
  
  print(lang[KEYS.LOG_INS_SERVER_INSTALLING])
  if Config.server_type == 'paper':
    paper_url = paper.get_latest_download_url(Config.server_version)
    
    print(lang[KEYS.LOG_INS_SERVER_PAPER_DOWNLOADING].format(paper_url))
    if paper_url:
      util.download_file(paper_url)
  else:
    print(
      lang[KEYS.LOG_INS_SERVER_TYPE_NOT_FOUND]
      .format(Config.server_type)
    )

def install() -> None:
  """Install Java, Minecraft server and plugins...
  """
  install_java()
  
  # Install Minecraft Server (TODO)
  install_server()

def init() -> None:
  """Initialize the installer
  """
  lock.run_thread_locker()

def close(code: int = 0) -> None:
  """Free stuff I guess
  """
  lock.unlock()
  _ = input(lang[KEYS.LOG_PROGRAM_COMPLETE])
  exit(code)
  
def main() -> None:
  """The installer/updater starts here
  """
  init()
  
  print_title()
  install()
  
  close()

def _start() -> None:
  """The executable starts here
  """
  _init()
  time_left = lock.lock()
  if not time_left: 
    main()
  else:
    print(lang[KEYS.LOG_ERR_ALREADY_RUNNING].format(time_left))
    exit(1)
  

if __name__ == '__main__':
  # To handle Ctrl + C (because of multithreading making it broken)
  __default_handler = signal.getsignal(signal.SIGINT)
  signal.signal(signal.SIGINT, __handle_interrupt)
  
  _start()
  
  