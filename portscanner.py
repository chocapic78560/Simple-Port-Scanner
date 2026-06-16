import socket

PORTS_A_SCANNER={
	21:"FTP",
	22:"SSH",
	23:"TELNET",
	80:"HTTP",
	443:"HTTPS",
	445:"SMB",
	110:"POP3"
}

for port in PORTS_A_SCANNER.keys():
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	result=s.connect_ex(("localhost", port))
	if result==0:
		print(f"Port {port} ({PORTS_A_SCANNER[port]}) is open.")
	else:
		print(f"Port {port} ({PORTS_A_SCANNER[port]}) is closed.")