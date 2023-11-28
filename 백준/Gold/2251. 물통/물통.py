import sys

a,b,c = map(int,sys.stdin.readline().split())
visit = [[0]*(b+1) for _ in range(a+1)]
ans = []
stack = []

def check(x,y):
    if 0<=x<=a and 0<=y<=b:
        if visit[x][y]==0:
            visit[x][y]=1
            stack.append((x,y))

check(0,0)
def dfs():
    
    while stack:
        x,y = stack.pop()
        z = c-x-y
        
        if x==0:
            ans.append(z)
            
        water = min(x,b-y)
        check(x-water,y+water)
        water = min(x,c-z)
        check(x-water,y)
            
        water = min(y,a-x)
        check(x+water,y-water)
        water = min(y,c-z)
        check(x,y-water)
            
        water = min(z,a-x)
        check(x+water,y)
        water = min(z,b-y)
        check(x,y+water)
        
dfs()
print(*sorted(ans))