"""
Main HTTP Server - Entry point for TCP connections
"""

import socket
import threading
from http_parser import parse_http_request
from router import get_handler
from response import build_response
from utils import log_request, handle_error

class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8080, use_threading=True):
        self.host = host
        self.port = port
        self.use_threading = use_threading
        self.server_socket = None
        self.running = False

    def start(self):
        """Start the HTTP server"""
        print(f"Starting HTTP server on {self.host}:{self.port}")
        
        # Create TCP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        
        print(f"Server listening on http://{self.host}:{self.port}")
        
        self.running = True
        try:
            while self.running:
                # Accept incoming connections
                client_socket, address = self.server_socket.accept()
                print(f"Connection from {address}")
                
                if self.use_threading:
                    # Handle each client in a separate thread
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, address)
                    )
                    client_thread.start()
                else:
                    self.handle_client(client_socket, address)
                    
        except KeyboardInterrupt:
            print("\nShutting down server...")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket, address):
        """Handle a single client connection"""
        try:
            # Receive data from client
            data = client_socket.recv(4096).decode('utf-8')
            
            if not data:
                return
                
            # Parse the HTTP request
            method, path, version, headers, body = parse_http_request(data)
            
            # Log the request
            log_request(method, path, address)
            
            # Get handler for the path
            handler = get_handler(path)
            
            # Execute handler and get response
            status_code, response_headers, response_body = handler(method, path, headers, body)
            
            # Build HTTP response
            response = build_response(status_code, response_headers, response_body)
            
            # Send response
            client_socket.send(response.encode('utf-8'))
            
        except Exception as e:
            # Handle errors
            error_response = handle_error(e)
            client_socket.send(error_response.encode('utf-8'))
            
        finally:
            client_socket.close()

def main():
    server = HTTPServer()
    server.start()

if __name__ == "__main__":
    main()