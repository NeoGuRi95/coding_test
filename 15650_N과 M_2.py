n, depth = map(int, input().split())
def dfs(lst, now_depth):
    if now_depth == depth:
        print(' '.join(str(i) for i in lst))
    else:
        for i in range(1, n+1):
            if len(lst) == 0:
                new_lst = lst.copy()
                new_lst.append(i)
                dfs(new_lst, now_depth + 1)
            elif i > lst[-1]:
                new_lst = lst.copy()
                new_lst.append(i)
                dfs(new_lst, now_depth + 1)
lst = []
now_depth = 0
dfs(lst, now_depth)

# input: 4 4
# output
# 1 2 3 4
#
# input: 4 2
# output
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4