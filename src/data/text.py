class KEYS:
  # General
  EXE_DESCRIPTION: str = 'exe.description'
  
  # Args
  ARGS_HELP_JAVA_VERSION: str = 'args.help.java_version'
  
  ARGS_HELP_SERVER_TYPE: str = 'args.help.server_type'
  ARGS_HELP_SERVER_VERSION: str = 'args.help.server_version'
  
  ARGS_HELP_SERVER_PATH: str = 'args.help.server_path'
  
  

en:dict[str, str] = {
  KEYS.EXE_DESCRIPTION: 'Install the Tikfinity custom Minecraft server',
  
  KEYS.ARGS_HELP_JAVA_VERSION : 'Specify the java version to download',
  KEYS.ARGS_HELP_SERVER_TYPE : 'Specify the Minecraft Server to download',
  KEYS.ARGS_HELP_SERVER_VERSION : 'Specify the Minecraft Server version to download',
  
  KEYS.ARGS_HELP_SERVER_PATH : 'Specify the path for the Minecraft Server',
  
}

lang:dict[str, str] = en