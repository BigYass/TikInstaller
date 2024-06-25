import os
import subprocess
import jdk
import ctypes
import winreg as reg

from data.text import lang, KEYS

def have_java() -> bool:
  """Detects if java is installed by running java -version

  Returns:
      bool: If java -version succeed
  """
  result = 1
  with open(os.devnull, 'wb') as devnull:  
    try:
      result = subprocess.check_call(['java', '-version'], stdout=devnull, stderr=devnull)
    except:
      return False
  return result == 0

def _add_java_path(java_home:str) -> None:
  """Add java_home to JAVA_HOME environment variable and the bin directory to PATH

  Args:
      java_home (str): JAVA_HOME of java newly installed
  """
  
  # Check if java_home directory exists
  if not os.path.isdir(bin_path):
    print(lang[KEYS.LOG_ERR_NOT_DIR].format(bin_path))
    return 
  
  os.environ['JAVA_HOME'] = java_home
  bin_path = os.path.join(java_home, 'bin')
  # Get current PATH
  current_path = ""
  with reg.OpenKey(reg.HKEY_CURRENT_USER, r'Environment', 0, reg.KEY_READ) as key:
    try:
      current_path = reg.QueryValueEx(key, 'PATH')[0]
    except FileNotFoundError:
      return
  
  # Add bin_path to PATH if not already present
  if bin_path not in current_path:
    new_path = current_path + ";" + bin_path if current_path else bin_path
    with reg.OpenKey(reg.HKEY_CURRENT_USER, r'Environment', 0, reg.KEY_WRITE) as key:
      reg.SetValueEx(key, 'PATH', 0, reg.REG_EXPAND_SZ, new_path)
      print(lang[KEYS.LOG_INS_JAVA_ADDED_PATH].format(bin_path))
  else:
    print(lang[KEYS.LOG_INS_JAVA_ALREADY_IN_PATH].format(bin_path))
    
  print(lang[KEYS.LOG_INS_JAVA_ADDED_PATH])
  # Add JAVA_HOME to registry
  try:
    with reg.OpenKey(reg.HKEY_CURRENT_USER, r'Environment', 0, reg.KEY_WRITE) as key:
      reg.SetValueEx(key, 'JAVA_HOME', 0, reg.REG_EXPAND_SZ, java_home)
      print(lang[KEYS.LOG_INS_JAVA_HOME_SET].format(java_home))
  except Exception as e:
    print(lang[KEYS.LOG_INS_ERR_JAVA_HOME].format(e))
    
  os.environ.update()

def get_java_path() -> str | None:
  """Try to find java home path

  Returns:
      str | None: Java path if found
  """
  path = os.environ.get('JAVA_HOME')
  if path and os.path.isdir(path):
    path = os.path.join(path, 'bin', 'java.exe')
    if os.path.isfile(path):
      return path
    
  return None

def install_java(version: str) -> str:
  """Install the targeted version of java

  Args:
      version (str, optional): Java version. Defaults to '17'.

  Returns:
      str: _description_
  """
  java_path = jdk.install(version)
  
  print(lang[KEYS.LOG_INS_JAVA_ADDING_PATH])
  _add_java_path(java_path)
  
  return java_path

