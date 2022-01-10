
n = int(input())
m = int(input())
s = input().rstrip()

def check(pos, n):
    if pos + n * 2 > len(s)-1:
        return False
    else:
        if s[pos:pos+n*2] == 'OI'*n:
            return True
        else:
            return False

cnt=0
for i in range(len(s)):
    if s[i]=="I":
        if check(i+1, n):
            cnt+=1
print(cnt)

