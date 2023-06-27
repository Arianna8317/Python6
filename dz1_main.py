from dz1 import if_date
import sys

if len(sys.argv) > 1:
    print(if_date(sys.argv[1]))
else:
    print(if_date())   