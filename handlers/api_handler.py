import json

def api_handler(method, path, headers, body):
    """
    Handle API requests
    """
    # Sample API response
    data = {
        'message': 'Hello from the API!',
        'method': method,
        'path': path,
        'server': 'MyHTTPServer/1.0'
    }
    
    response_body = json.dumps(data, indent=2)
    
    response_headers = {
        'Content-Type': 'application/json',
        'Server': 'MyHTTPServer/1.0'
    }
    
    return 200, response_headers, response_body
