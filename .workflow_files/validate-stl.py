#!python3
import sys
from admesh import Stl
import tweaker3.FileHandler as fh
from tweaker3.MeshTweaker import Tweak

file_handler = fh.FileHandler()

def process_stl(filename: str) -> bool:
    stl = Stl(filename)
    stl.repair(verbose_flag=False)
    if stl.stats['edges_fixed'] > 0 or stl.stats['backwards_edges'] > 0 or stl.stats['degenerate_facets'] > 0 or stl.stats['facets_removed'] > 0 or stl.stats['facets_added'] > 0 or stl.stats['facets_reversed'] > 0:
      print(f"\tCorrupt STL detected! Please fix {filename}!")
      return False
    return True

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
      if process_stl(argument) and check_stl_rotation(argument):
        sys.exit(0)
      else:
        sys.exit(0) # ToDo Fixme

if __name__ == "__main__":
   main(sys.argv[1:])
