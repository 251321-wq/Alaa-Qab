# port_report.py
# Classify a range of port numbers and count how many were checked.
start_port = int(input("Start port: "))
end_port = int(input("End port: "))
ports_checked = 0

for port in range(start_port, end_port + 1):
    if 0 <= port <= 1023:
        category = "system"
    elif 1024 <= port <= 49151:
        category = "user"
    elif 49152 <= port <= 65535:
        category = "dynamic"
    else:
        category = "outside the valid port range"
    print(f"{port}: {category}")
    ports_checked += 1

print(f"Ports checked: {ports_checked}")
