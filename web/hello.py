def application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    data = environ.get('QUERY_STRING').replace('&', '\n')
    start_response(status, headers)
    return [bytes(data, 'utf-8')]
