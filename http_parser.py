"""
HTTP Request Parser - Parses raw HTTP requests
"""

def parse_http_request(data):
    """
    Parse raw HTTP request data
    Returns: (method, path, version, headers, body)
    """
    if not data:
        return None, None, None, {}, ""
    
    # Split request into lines
    lines = data.split('\r\n')
    
    # Parse request line (first line)
    request_line = lines[0].split(' ')
    if len(request_line) < 3:
        return None, None, None, {}, ""
    
    method = request_line[0]
    path = request_line[1]
    version = request_line[2]
    
    # Parse headers
    headers = {}
    body_start_index = 0
    
    for i in range(1, len(lines)):
        line = lines[i]
        
        # Empty line indicates end of headers
        if line == '':
            body_start_index = i + 1
            break
            
        # Parse header
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
    
    # Extract body if present
    body = ''
    if body_start_index < len(lines):
        body = '\r\n'.join(lines[body_start_index:])
    
    return method, path, version, headers, body