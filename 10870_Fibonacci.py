n = int(input())
def fivonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fivonacci(n-1) + fivonacci(n-2)

def fiv_iter(n):
    if n == 0: return 0
    if n == 1: return 1

    pp = 0
    p = 1
    for i in range(n-1):
        answer = pp + p
        pp = p
        p = answer
    return answer

answer1 = fivonacci(n)
print(answer1)
answer2 = fiv_iter(n)
print(answer2)