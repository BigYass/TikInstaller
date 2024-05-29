from os import path
from data.info import name

local = path.join(path.expandvars(r'%APPDATA%'), name)

servers = path.join(local, 'Servers')

lock_file = path.join(local, f'{name}.lock')