#https://codeforces.com/problemset/problem/208/A

W = input()

N = ""
lt = "abc"

for w in W:

    lt = lt[1:] + w
    if lt == "WUB":
        N = N[:-2]
        if N != "" and N[-1] != " ":
            N += " "

    else:   
        N += w

print(N)
