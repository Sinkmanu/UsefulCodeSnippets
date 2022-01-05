#!/usr/bin/env python3

import hashlib
import sys
import binascii

seed = sys.argv[1].encode('utf-8')

md = [0]*1003
msg = [0]*1003
for i in range(0, 99):
    md[0] = md[1] = md[2] = seed
    for j in range(3, 1003):
        msg[j] = md[j-3] + md[j-2] + md[j-1]
        msg_t = binascii.unhexlify(msg[j])
        md[j] = hashlib.sha224(msg_t).hexdigest().encode('utf-8')
    seed = md[1002]
    print("%i : %s" % (i, seed))
