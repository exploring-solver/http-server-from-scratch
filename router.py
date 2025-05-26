"""
Router - Maps URL paths to handler functions
"""

from handlers.index_handler import index_handler
from handlers.api_handler import api_handler
from handlers.static_handler import static_handler
from handlers.not_found_handler import not_found_handler

# Define route table
ROUTES = {
    '/': index_handler,
    '/api': api_handler,
    '/api/data': api_handler,
}

def get_handler(path):
    """
    Get handler function for given path
    """
    # Check if path is for static files
    if path.startswith('/static/'):
        return static_handler
    
    # Look up handler in route table
    handler = ROUTES.get(path)
    
    if handler:
        return handler
    
    # Default to 404 handler
    return not_found_handler