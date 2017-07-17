bind = '0.0.0.0:8080'

def hello_app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    import pdb; pdb.set_trace() 
