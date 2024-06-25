class KEYS:
  # General
  EXE_DESCRIPTION: str = 'exe.description'
  EXE_MADE_BY: str = 'exe.made_by'
  EXE_VERSION: str = 'exe.version'
  
  # Args
  ARGS_HELP_JAVA_VERSION: str = 'args.help.java_version'
  
  ARGS_HELP_SERVER_TYPE: str = 'args.help.server_type'
  ARGS_HELP_SERVER_VERSION: str = 'args.help.server_version'
  
  ARGS_HELP_SERVER_PATH: str = 'args.help.server_path'
  
  # Installation
  INS_SHORTCUT_SERVER_DESCRIPTION: str = 'ins.shortcut.server_description'
  
  # Installation logs
  LOG_INS_JAVA_INSTALLING: str = 'log.ins.java.installing'
  LOG_INS_JAVA_SEARCHING: str = 'log.ins.java.searching'
  LOG_INS_JAVA_NOT_FOUND: str = 'log.ins.java.not_found'
  LOG_INS_JAVA_INSTALLED: str = 'log.ins.java.installed'
  LOG_INS_JAVA_FOUND: str = 'log.ins.java.found'
  
  LOG_INS_JAVA_ADDING_PATH: str = 'log.ins.java.adding_path'
  LOG_INS_JAVA_ADDED_PATH: str = 'log.ins.java.added_path'
  LOG_INS_JAVA_ALREADY_IN_PATH: str = 'log.ins.java.already_path'
  LOG_INS_JAVA_HOME_SETTING: str = 'log.ins.java.home_setting'
  LOG_INS_JAVA_HOME_SET: str = 'log.ins.java.home_set'
  
  LOG_INS_SERVER_TYPE_NOT_FOUND: str = 'log.ins.server'
  LOG_INS_SERVER_INSTALLING: str = 'log.ins.server.installing'
  LOG_INS_SERVER_PAPER_DOWNLOADING: str = 'log.ins.server.paper.downloading'
  
  
  
  # Installation errors
  LOG_INS_ERR_NOT_DIR: str = 'log.ins.err.not_dir' 
  LOG_INS_ERR_JAVA_HOME: str = 'log.ins.err.java_home'
  
  # General Logs
  LOG_PROGRAM_COMPLETE: str = 'log.program_complete'
  

  # Errors logs
  LOG_ERR_ALREADY_RUNNING: str = 'log.err.already_running'
  
  

en:dict[str, str] = {
  #General
  KEYS.EXE_DESCRIPTION: 'Install the Tikfinity custom Minecraft server',
  KEYS.EXE_MADE_BY: 'Made by {0}',
  KEYS.EXE_VERSION: 'Version {0}',
  
  # Args
  KEYS.ARGS_HELP_JAVA_VERSION : 'Specify the java version to download',
  KEYS.ARGS_HELP_SERVER_TYPE : 'Specify the Minecraft Server to download',
  KEYS.ARGS_HELP_SERVER_VERSION : 'Specify the Minecraft Server version to download',
  
  #Installation
  KEYS.INS_SHORTCUT_SERVER_DESCRIPTION : 'Run the minecraft server',
  
  # Installation logs
  KEYS.LOG_INS_JAVA_INSTALLING: 'Installing Java ({0})...',
  KEYS.LOG_INS_JAVA_SEARCHING: 'Searching Java',
  KEYS.LOG_INS_JAVA_NOT_FOUND: 'Java not found, installing...',
  KEYS.LOG_INS_JAVA_INSTALLED: 'Java installed at {0}',
  KEYS.LOG_INS_JAVA_FOUND: 'Java found at {0}',
  
  KEYS.LOG_INS_JAVA_ADDING_PATH: 'Adding java to PATH...', 
  KEYS.LOG_INS_JAVA_ADDED_PATH: 'Added {0} to PATH', 
  KEYS.LOG_INS_JAVA_ALREADY_IN_PATH: '{0} already in PATH',
  KEYS.LOG_INS_JAVA_HOME_SETTING: 'Setting JAVA_HOME', 
  KEYS.LOG_INS_JAVA_HOME_SET: 'JAVA_HOME set to {0}',
  
  KEYS.LOG_INS_SERVER_TYPE_NOT_FOUND: '{0} server uknown, quiting...',
  
  KEYS.LOG_INS_SERVER_INSTALLING: 'Starting the server installation',
  KEYS.LOG_INS_SERVER_PAPER_DOWNLOADING: 'Downloading paper.jar ({0})',
  
  # Installation errors
  KEYS.LOG_INS_ERR_NOT_DIR: '{0} does not exists or is not a directory...',
  KEYS.LOG_INS_ERR_JAVA_HOME: 'Error writing JAVA_HOME to registry: {0}',
  
  # General logs
  KEYS.LOG_PROGRAM_COMPLETE : 'Program complete, press Enter to exit...',

  # Errors logs
  KEYS.LOG_ERR_ALREADY_RUNNING : 'Installer already running, quiting... ({0})',
}

lang:dict[str, str] = en