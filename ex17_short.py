from sys import argv
from os.path import exists

# This attempt in one line is naught for a few reasons:
#   *It does not ask for the user's permission first
#   *It does not close either file.
open(argv[2], 'w').write(open(argv[1]).read())
