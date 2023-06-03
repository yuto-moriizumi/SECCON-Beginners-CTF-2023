# coding: utf-8
import random
import os
import math
from typing import List
import re

flag = b"ctf4b{xxx___censored___xxx}"

reg = re.compile("ctf4b{[\x20-\x7e]+}")

# flag = b"ctf4b{xxx"
# 44文字

# Please remove here if you wanna test this code in your environment :)
# flag = os.getenv("FLAG").encode()


cipher = []

for i in range(len(flag) - 1):
    c = (flag[i] + flag[i + 1]) ** 2 + i
    cipher.append(c)

random.shuffle(cipher)

print(f"cipher = {cipher}")

cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293,
          38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]

result = []


def solve(prev: int, index: int, c: int, flags: List[int], ciphers: List[int]):
    diff = math.sqrt((c - index))
    if(not diff.is_integer()):
        return
    val = int(diff-prev)
    if(val < 0 or val < 0x20 or 0x7e < val):
        return
    flags.append(val)
    for i in range(len(ciphers)):
        cip = ciphers[i]
        left = ciphers[0:i]
        if(i+1 < len(ciphers)):
            left.extend(ciphers[i+1:])
        solve(val, index+1, cip, flags, left)
    if(len(ciphers) == 0):
        res = bytes(flags).decode('utf-8')
        if(reg.fullmatch(res)):
            result.append(bytes(flags).decode('utf-8'))
    flags.pop()


startCharacter = int.from_bytes(b"c", 'big')

cipher.remove(46225)
solve(startCharacter, 0, 46225, [startCharacter], cipher)

print(result)
