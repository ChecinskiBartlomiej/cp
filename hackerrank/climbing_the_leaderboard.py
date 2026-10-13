#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

def climbingLeaderboard(ranked, player):
    unique = list(dict.fromkeys(ranked))

    k = len(unique) - 1
    o = []
    for j in range(len(player)):

        while (k>=0) and (player[j] >= unique[k]):
            k -= 1
        place = k + 2
        o.append(place)

    return o
