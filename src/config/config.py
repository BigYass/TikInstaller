from config.args import args

class config:
  java_version: str  = args.java_version
  server_version: str = args.server_version
  server_type: str['paper'] = args.server_type
  