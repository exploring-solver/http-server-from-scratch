"""
Utility functions
"""

import datetime

def get_mime_type(filename):
    """
    Get MIME type based on file extension
    """
    mime_types = {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.json': 'application/json',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon',
        '.txt': 'text/plain',
    }
    
    # Get file extension
    ext = filename[filename.rfind('.'):].lower()
    
    return mime_types.get(ext, 'application/octet-stream')

def log_request(method, path, address):
    """
    Log HTTP request
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {address[0]}:{address[1]} - {method} {path}")

def handle_error(error):
    """
    Generate error response
    """
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 Internal Server Error</h1>
    <p>An error occurred: {str(error)}</p>
</body>
</html>"""
    
    response = f"HTTP/1.1 500 Internal Server Error\r\n"
    response += "Content-Type: text/html\r\n"
    response += f"Content-Length: {len(html_content)}\r\n"
    response += "\r\n"
    response += html_content
    
    return response