#!python3
import sys
from admesh import Stl

def process_stl(filename: str) -> bool:
    stl = Stl(filename)
    stl.repair(verbose_flag=False)
    if stl.stats['edges_fixed'] > 0 or stl.stats['backwards_edges'] > 0 or stl.stats['degenerate_facets'] > 0 or stl.stats['facets_removed'] > 0 or stl.stats['facets_added'] > 0 or stl.stats['facets_reversed'] > 0:
      print(f"\tCorrupt STL detected! Please fix {filename}!")
      return False
    return True
        
def main(argv):
    argument = " ".join(sys.argv[1:])
    print(f"Checking {argument}")
    if argument.lower().endswith(".stl"):
      if process_stl(argument):
        sys.exit(0)
      else:
        sys.exit(0) # ToDo Fixme

if __name__ == "__main__":
   main(sys.argv[1:])
