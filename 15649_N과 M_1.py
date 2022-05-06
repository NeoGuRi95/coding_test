def dfs(n, depth, history, now_depth):
    if now_depth == depth:
        print(' '.join(str(i) for i in history))
    else:
        for i in range(1, n + 1):
            if i not in history:
                new_history = history.copy()
                new_history.append(i)
                dfs(n, depth, new_history, now_depth + 1)


n, depth = map(int, input().split())
dfs(n, depth, [], 0)

# input: 4 4
# output
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# 2 4 3 1
# 3 1 2 4
# 3 1 4 2
# 3 2 1 4
# 3 2 4 1
# 3 4 1 2
# 3 4 2 1
# 4 1 2 3
# 4 1 3 2
# 4 2 1 3
# 4 2 3 1
# 4 3 1 2
# 4 3 2 1