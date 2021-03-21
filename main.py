from intro import print_intro
from commander import commander
import sys

if len(sys.argv) == 1:
    print_intro()
else:
    command = sys.argv[1:]
    commander(command)
