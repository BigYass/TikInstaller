import os, winshell
import requests
import ctypes
from data.text import lang, KEYS
from win32com.client import Dispatch

def add_shortcut(target: str, name:str, to: str = winshell.desktop()) -> None:
  to = os.path.join(to, f'{name}.lnk')
  
  shell = Dispatch('WScript.Shell')
  shortcut = shell.CreateShortcut(to)
  shortcut.Targetpath = target 
  shortcut.WorkingDirectory = os.path.dirname(target)
  shortcut.IconLocation = target
  shortcut.Description = lang[KEYS.INS_SHORTCUT_SERVER_DESCRIPTION]
  
def download_file(url: str, to: str) -> None:
  r = requests.get(url)
  
  r.raise_for_status()
  
  with open(to, 'wb') as f:
    f.write(r.content)

  
 
def is_admin() -> bool:
  """Checks if is launched as admin

  Returns:
      bool: Is admin
  """
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False