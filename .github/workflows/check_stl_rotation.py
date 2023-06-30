#!python3
import sys
import tweaker3.FileHandler as fh
from tweaker3.MeshTweaker import Tweak

file_handler = fh.FileHandler()

def check_stl_rotation(filename: str) -> bool:
    objs = file_handler.load_mesh(filename)
    for part, content in objs.items():
        x = Tweak(content["mesh"], extended_mode=True, verbose=False)
        if x.rotation_angle >= 0.1:
          print(f"\tPossible bad orientation of STL detected! Please check orientation of {filename}!")
          return False
    return True
        
def main(argv):
    argument = " ".join(sys.argv[1:])
    print(f"Checking {argument}")
    if argument.lower().endswith(".stl"):
      if check_stl_rotation(argument):
        sys.exit(0)
      else:
        sys.exit(0) # ToDo Fixme

if __name__ == "__main__":
   main(sys.argv[1:])
