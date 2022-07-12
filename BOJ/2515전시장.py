n,s = map(int, input().split())
paintings = [(0,0) for _ in range(n)]
DP = [[0*2] for _ in range(n)]
for i in range(n):
    h, c = map(int, input().split())
    paintings[i] = (h,c)


paintings = sorted(paintings,key=lambda x:x[0], reverse=True)
DP[0][0] = paintings[0][0]


import socket
s = socket.socket()
s.bind(("",80))
s.listen(0)
while True:
    client, addr = s.accept()
    while True:
        content = client.recv(32)