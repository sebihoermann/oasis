from __future__ import print_function
import sys
import os

if not os.path.isfile("update.txt"):
    print("Run the \"updater\" command in oasis first!")
    sys.exit(1)

print("Finishing update...")
print("Removing update.txt...")
os.remove("update.txt")
print("Removing main.py...")
os.remove("main.py")
print("Renaming new-main.py to main.py...")
os.rename("new-main.py", "main.py")
print("\n")
print("Successfully updated oasis")
