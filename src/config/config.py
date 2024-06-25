from config.args import args

class Config:
  java_version: str  = args.java_version or '17'
  server_version: str = args.server_version or 'latest'
  server_type: str = args.server_type or 'paper'
  