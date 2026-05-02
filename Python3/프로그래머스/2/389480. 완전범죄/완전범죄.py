def solution(info, n, m):
    global minlen
    arr1 = []
    arr2 = []
    minlen = 1e9
    visited = set()
    def dfs(a, b, now):
        global minlen
        if a >= n or b >= m:
            return

        if (a,b,now) in visited:
            return
        else:
            visited.add((a,b,now))
        
        if now == len(info):
            minlen = min(minlen, a)
            return

        dfs(a + info[now][0], b, now + 1)
        dfs(a, b + info[now][1], now + 1)

    dfs(0, 0, 0)
    answer = minlen
    if answer > 1e8:
        answer = -1

    return answer