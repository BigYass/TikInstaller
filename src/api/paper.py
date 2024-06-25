import requests

__url = 'https://api.papermc.io'

class Download:
  def __init__(self, _json) -> None:
    self.name: str = _json['name']
    self.sha256: str = _json['sha256']

class Change:
  def __init__(self, _json) -> None:
    self.commit: str = _json['commit']
    self.summary: str = _json['summary']
    self.message: str = _json['message']
    
class VersionBuild:
  def __init__(self, _json) -> None:
    self.build: int = int(_json['build'])
    self.time: str = _json['time']
    
    self.channel: str['default', 'experimental'] = _json['channel']
    self.promoted: bool = bool(_json['promoted'])
    
    self.changes: list[Change] = [Change(i) for i in _json["changes"]]
    
    self.downloads: Download = Download(_json['downloads']['application'])

class BuildResponse:
  def __init__(self, _json) -> None:
    self.project_id: str = _json["project_id"]
    self.project_name: str = _json["project_name"]
    self.version: str = _json["version"]
    
    self.build: int = int(_json["build"])
    
    self.time: str = _json["time"]
    self.channel: str['default' | 'experimental'] = _json["channel"]
    
    self.promoted: bool = bool(_json["promoted"])
    self.changes: list[Change] = [Change(i) for i in _json["changes"]]
    self.downloads: Download = Download(_json['downloads']['application'])
    
class BuildsResponse:
  def __init__(self, _json) -> None:
    self.project_id: str = _json["project_id"]
    self.project_name: str = _json["project_name"]
    self.version: str = _json["version"]
    self.builds: list[VersionBuild] = [VersionBuild(i) for i in _json["builds"]]
    
class ProjectResponse:
  def __init__(self, _json) -> None:
    self.project_id: str = _json["project_id"]
    self.project_name: str = _json["project_name"]
    self.version_groups: list[str] = _json["version_groups"]
    self.versions: list[str] = _json["versions"]
    
    
class ProjectsResponse:
  def __init__(self, _json) -> None:
    self.project_id: list[str] = _json["project_id"]
    
class VersionFamilyBuild:
  def __init__(self, _json) -> None:
    self.version: str = _json["version"]
    
    self.build: int = int(_json["build"])
    
    self.time: str = _json["time"]
    self.channel: str['default' | 'experimental'] = _json["channel"]
    
    self.promoted: bool = bool(_json["promoted"])
    self.changes: list[Change] = [Change(i) for i in _json["changes"]]
    self.downloads: Download = Download(_json['downloads']['application'])
    
class VersionFamilyBuildsResponse:
  def __init__(self, _json) -> None:
    self.project_id: str = _json["project_id"]
    self.project_name: str = _json["project_name"]
    
    self.version_group: str = _json['version_group']
    
    self.versions: list[str] = _json["versions"]
    self.builds: VersionFamilyBuild = [VersionFamilyBuild(i) for i in _json['builds']]
    
class VersionFamilyResponse:
  def __init__(self, _json) -> None:
    self.project_id: str = _json["project_id"]
    self.project_name: str = _json["project_name"]
    
    self.version_group: str = _json["version_group"]
    
    self.project_id: list[str] = _json["project_id"]
  
class VersionResponse:
  def __init__(self, _json) -> None:
    self.project_id: str = _json["project_id"]
    self.project_name: str = _json["project_name"]
    self.version: str = _json["version"]
    
    self.builds: list[int] = [int(i) for i in _json["build"]]
    
  
async def get_projects() -> ProjectsResponse:
  full_url = f'{__url}/v2/projects'
  
  r = requests.get(full_url)
  
  r.raise_for_status()
  
  return ProjectsResponse(r.json())
  
async def get_project(project:str = 'paper') -> ProjectResponse:
  full_url = f'{__url}/v2/projects/{project}'
  
  r = requests.get(full_url)
  
  r.raise_for_status()
  
  return ProjectResponse(r.json())
  
async def get_version(version: str, project:str = 'paper') -> VersionResponse:
  full_url = f'{__url}/v2/projects/{project}/versions/{version}'
  
  r = requests.get(full_url)
  
  r.raise_for_status()
  
  return VersionResponse(r.json())
  
async def get_builds(version: str, project:str = 'paper') -> BuildsResponse:
  full_url = f'{__url}/v2/projects/{project}/versions/{version}/builds'

  r = requests.get(full_url)
  
  r.raise_for_status()
  
  return BuildsResponse(r.json())
  
async def get_build(build: int, version: str, project:str = 'paper') -> BuildResponse:
  full_url = f'{__url}/v2/projects/{project}/versions/{version}/builds/{build}'

  r = requests.get(full_url)
  
  r.raise_for_status()
  
  return BuildResponse(r.json())
  
def get_download(download: str, build: int, version: str, project:str = 'paper') -> str:
  return f'{__url}/v2/projects/{project}/versions/{version}/builds/{build}/downloads/{download}'

async def get_version_group(family:str, project:str = 'paper') -> VersionFamilyResponse:
  full_url = f'{__url}/v2/projects/{project}/version_group/{family}'

  r = requests.get(full_url)
  
  r.raise_for_status()
  
  return VersionFamilyResponse(r.json())
  
async def get_builds_group(family: str, project:str = 'paper') -> VersionFamilyBuildsResponse:
  full_url = f'{__url}/v2/projects/{project}/version_group/{family}/builds'

  r = requests.get(full_url)
  
  r.raise_for_status()
  
  return VersionFamilyBuildsResponse(r.json())
  
async def get_latest_download_url(version: str | None = None, project: str = 'paper') -> str:
  if version.lower() == 'latest':
    version = None
  
  ver = version or (await get_project()).versions[-1]
  
  b = await get_builds(ver)
  
  build = b.builds[-1].build
  
  download = b.builds[-1].downloads.name
  
  return get_download(download, build, ver)
