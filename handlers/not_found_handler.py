"""
404 Not Found handler
"""

def not_found_handler(method, path, headers, body):
    """
    Handle 404 errors
    """
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The requested resource was not found on this server.</p>
</body>
</html>"""
    
    headers = {
        'Content-Type': 'text/html',
        'Server': 'MyHTTPServer/1.0'
    }
    
    return 404, headers, html_content