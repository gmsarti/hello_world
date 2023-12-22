import os
from pathlib import Path

def print_directory_structure(path, level=0, file=None):
  # Ignore .env directory and Git files
  if '.env' in path.parts or '.git' in path.parts:
      return

  indent = '│ ' * level
  if file is None:
      print(indent + str(path))
  else:
      file.write(indent + str(path) + '\n')

  for child in path.iterdir():
      if child.is_dir():
          print_directory_structure(child, level+1, file)
      elif child.is_file():
          file.write(indent + '└── ' + child.name + '\n')

with open('structure.txt', 'w', encoding='utf-8') as file:
  print_directory_structure(Path('.'), file=file)
