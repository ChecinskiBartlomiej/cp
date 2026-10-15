#https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true

def twoPluses(grid):
    # Write your code here
    def is_valid_plus(n,m,i,j,k,grid):
        d=(k-1)//2
        if (i-d<0) or (i+d>n-1) or (j-d<0) or (j+d>m-1):
            return False
        if grid[i][j]=="B":
            return False
        for a in range(1,d+1):
            if (grid[i-a][j]=="B") or (grid[i+a][j]=="B") or (grid[i][j-a]=="B") or (grid[i][j+a]=="B"):
                return False
        return True

    def find_all_pluses(grid):
        pluses = []
        n=len(grid)
        m=len(grid[0])
        s=min(n,m)
        for i in range(n):
            for j in range(m):
                for k in range(1, s+1):
                    if k%2==1:
                        if is_valid_plus(n,m,i,j,k,grid)==False:
                            break
                        else:
                            pluses.append(((i,j),k))
        return pluses

    def is_overlap(p1,p2):
        i1,j1=p1[0]
        d1=(p1[1]-1)//2

        i2,j2=p2[0]
        d2=(p2[1]-1)//2

        cells1={(i1,j1)}
        cells2={(i2,j2)}

        for a in range(1,d1+1):
            cells1.add((i1-a,j1))
            cells1.add((i1+a,j1))
            cells1.add((i1,j1-a))
            cells1.add((i1,j1+a))

        for a in range(1,d2+1):
            cells2.add((i2-a,j2))
            cells2.add((i2+a,j2))
            cells2.add((i2,j2-a))
            cells2.add((i2,j2+a))

        return len(cells1&cells2)>0


    def find_area_from_length(s):
        return 1+((s-1)//2)*4

    pluses=find_all_pluses(grid)
    M=0
    for j in range(len(pluses)):
        for k in range(j+1, len(pluses)):
            if is_overlap(pluses[j],pluses[k])==False:
                a1=find_area_from_length(pluses[j][1])
                a2=find_area_from_length(pluses[k][1])
                M=max(M,a1*a2)
    return M