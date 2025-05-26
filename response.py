"""
Response Builder - Constructs HTTP responses
"""

def build_response(status_code, headers, body):
    """
    Build HTTP response string
    """
    # Status line
    status_messages = {
        200: 'OK',
        404: 'Not Found',
        500: 'Internal Server Error'
    }
    
    status_message = status_messages.get(status_code, 'Unknown')
    response = f"HTTP/1.1 {status_code} {status_message}\r\n"
    
    # Add headers
    for key, value in headers.items():
        response += f"{key}: {value}\r\n"
    
    # Add content length
    if body:
        response += f"Content-Length: {len(body)}\r\n"
    
    # End of headers
    response += "\r\n"
    
    # Add body
    response += body
    
    return response