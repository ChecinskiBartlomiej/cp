count1 = [0] * 26
count2 = [0] * 26

a = input()
b = input()
c = input()

for l in a:
    count1[ord(l) - ord("A")] += 1
for l in b:
    count1[ord(l) - ord("A")] += 1
for l in c:
    count2[ord(l) - ord("A")] += 1

if count1 == count2:
    print("YES")
else:
    print("NO")
