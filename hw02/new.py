import socket

# 从stdin读取DNS名称
dns_names = []
while True:
    try:
        name = input()
        dns_names.append(name)
    except EOFError:
        break

# 翻译DNS名称为IP地址并打印输出
for name in dns_names:
    try:
        ip_addresses = socket.gethostbyname_ex(name)[-1]
        for ip in ip_addresses:
            print(ip)
    except socket.gaierror:
        print("Invalid DNS name:", name)
