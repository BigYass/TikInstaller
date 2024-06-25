import os
from config import path
from data import const

class Serializable:
  def toDict(self) -> dict[str, str]:
    raise NotImplementedError("toDict not implemented")
  
  def fromDict(self, _dict) -> super | None:
    raise NotImplementedError("fromDict not implemented")

class ServerSave(Serializable):
  def __init__(self, type: str, version: str, path: str, run_script: str) -> None:
    self.type: str = type
    self.version: str = version
    self.path: str = path 
    self.run_script: str = run_script
    
  def is_valid(self) -> bool:
    return os.path.isdir(self.path)
  
  def toDict(self) -> dict[str, str]:
    _dict:dict[str, str] = {
      'type': self.type,
      'version': self.version,
      'path': self.path,
    }
    return _dict
  
  def fromDict(self, _dict) -> super | None:
    try:
      return ServerSave(_dict['type'], _dict['version'], _dict['path'])
    except:
      return None
    
def add_server(name: str, version: str, type: str = 'paper', path: str = path.servers) -> ServerSave:
  pass # TODO