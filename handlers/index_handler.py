"""
Index page handler
"""

def index_handler(method, path, headers, body):
    """
    Handle requests to /
    """
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Welcome to My HTTP Server</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Welcome to My HTTP Server!</h1>
    <p>This server was built from scratch using Python sockets.</p>
    <p><a href="/api">Check out the API</a></p>
    <script src="/static/script.js"></script>
</body>
</html>"""
    
    headers = {
        'Content-Type': 'text/html',
        'Server': 'MyHTTPServer/1.0'
    }
    
    return 200, headers, html_content