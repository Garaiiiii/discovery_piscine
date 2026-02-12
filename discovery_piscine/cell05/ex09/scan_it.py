#!/usr/bin/env python3
import sys
if (len(sys.argv) !=  3):
        print("none")
else:
	print(f"{sys.argv[2].count(sys.argv[1])}")
