import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
sum = 0
b.sort()
a.sort(reverse=True)
for i in range(n):
    sum += a[i]*b[i]
print(sum)