#!/usr/bin/python3 

def app(environ, start_response):
    data = environ["QUERY_STRING"]
    data = "\n".join(data.split('&'))
    #data = 'Hello, world!'
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data.encode('utf-8')])
