s, n = map(int, input().split())
 
XY = []
 
for k in range(n):
    xy = list(map(int, input().split()))
    XY.append(xy)
 
XY.sort(key=lambda pair: pair[0])
 
def can_beat(s):
    for k in range(n):
        if s > XY[k][0]:
            s += XY[k][1]
        else:
            return False
    return True
 
if can_beat(s) == False:
    print("NO")
else:
    print("YES")