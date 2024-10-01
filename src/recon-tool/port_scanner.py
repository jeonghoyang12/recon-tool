import socket
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self, target):
        self.target = target

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((self.target, port))
        sock.close()
        if result == 0:
            return port
        return None
    
    def scan(self, start_port, end_port):
        open_ports = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(self.scan_port, port) for port in range(start_port, end_port + 1)]
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
        return open_ports
                