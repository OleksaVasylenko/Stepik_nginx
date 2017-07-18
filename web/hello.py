def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    data = environ.get('QUERY_STRING')
    start_response(status, headers)
    return [ data ]
