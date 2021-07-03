# Simple-Port-Scanner
A Python application that uses sockets to scan for open ports on a given host/ip.

## Dependencies
```sh
Python 3.8.7
```

## Usage
### port_scanner:  
**get_open_ports**("{**hostname/IP_address**}", [**start_port**, **end_port**], **verbose**=False)

```py
print( port_scanner.get_open_ports("104.26.10.78", [8079, 8090]) )

# returns:
[8080]

print( ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], verbose=True) )

# returns:
Open ports for hackthissite.org (137.74.187.104)
PORT     SERVICE
443      https
```
