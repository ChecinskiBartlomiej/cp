#https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true

def lilysHomework(arr):
    # Write your code here
    n = len(arr)

    inc = sorted(arr)
    dec = sorted(arr, reverse=True)


    def count_swaps(arr, ord_arr):
        d = {}
        for j in range(n):
            d[arr[j]] = j

        p = list(arr)
        l = 0
        for j in range(n):
            v = p[j]
            w = d[ord_arr[j]]
            if  v != p[w]:
                tmp = v
                p[j] = p[w]
                p[w] = tmp
                tmp = d[v]
                d[v] = w
                w = tmp
                l +=1
    
        return l

    return min(count_swaps(arr, inc), count_swaps(arr, dec))