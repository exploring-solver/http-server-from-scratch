"""
Static file handler
"""

import os
from utils import get_mime_type

def static_handler(method, path, headers, body):
    """
    Handle static file requests
    """
    # Remove /static/ prefix
    file_path = path[8:]  # Remove '/static/'
    
    # Security: prevent directory traversal
    if '..' in file_path:
        return 404, {}, 'Not Found'
    
    # Construct full file path
    full_path = os.path.join('static', file_path)
    
    try:
        # Read file
        with open(full_path, 'rb') as f:
            content = f.read()
        
        # Determine content type
        content_type = get_mime_type(file_path)
        
        response_headers = {
            'Content-Type': content_type,
            'Server': 'MyHTTPServer/1.0'
        }
        
        # Return as string if text file, otherwise bytes
        if content_type.startswith('text/'):
            return 200, response_headers, content.decode('utf-8')
        else:
            return 200, response_headers, content
            
    except FileNotFoundError:
        return 404, {}, 'Not Found'