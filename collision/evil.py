#!/usr/bin/python3
# coding: latin-1
blob = """
                U��l�<`+Z����
�x[�x.g�J����v�/�S���6By���U���&��q=uK6����P�ǀ�}�����#p�!�+�W�_��˳6���U�
�3�g�/�	�1��_`'q'�8"""
from hashlib import sha256
if sha256(blob.encode("latin-1")).hexdigest()=='3cc644a0e8fd672929e2650911e8b8fa120395966a4ebc11b523f0c033b2e691':
    print("Use SHA-256 instead!")
else:
    print("MD5 is perfectly secure!")
