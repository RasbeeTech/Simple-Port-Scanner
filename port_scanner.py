import socket
import re
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    address = ''
    hostname = ''

    # validate target
    if re.search('^[0-9\.]*$', target):
        try:
            name, alias, addresslist = socket.gethostbyaddr(target)
            address = target
            hostname = name
        except socket.herror:
            address = target
            hostname = None
        except socket.gaierror:
            return 'Error: Invalid IP address'
    else:
        try:
            address = socket.gethostbyname(target)
            hostname = target
        except socket.gaierror:
            return 'Error: Invalid hostname'
    
    try:
        # Scan ports
        for port in range(port_range[0], port_range[1]+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
    except socket.error:
        print("Couldn't connect to server")
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
    except socket.error:
        print ("Couldn't connect to server")
    
    if not verbose:
        # return [open_ports]
        return(open_ports)
    else:
        # Stringify
        string_builder = []
        if hostname:
            string_builder.append(f"Open ports for {hostname} ({address})")
        else:
            string_builder.append(f"Open ports for {address}")
        
        left = 'PORT'.ljust(9, ' ')
        right = 'SERVICE'
        string_builder.append(left + right)
        
        for port in open_ports:
          left = str(port).ljust(9, ' ')
          right = ports_and_services[port]
          string_builder.append(left + right)
        return '\n'.join(string_builder)
