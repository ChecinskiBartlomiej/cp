#https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true

def surfaceArea(A):
    # Write your code here
    H = len(A)
    W = len(A[0])

    s = 2 * H * W

    for i in range(H):
        for j in range(W):
            c = A[i][j]

            left  = A[i][j-1] if j > 0 else 0
            right = A[i][j+1] if j < W-1 else 0
            up    = A[i-1][j] if i > 0 else 0
            down  = A[i+1][j] if i < H-1 else 0

            s += max(0, c - left)
            s += max(0, c - right)
            s += max(0, c - up)
            s += max(0, c - down)

    return s
    



