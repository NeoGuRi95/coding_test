n = int(input())
def fivonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fivonacci(n-1) + fivonacci(n-2)
answer = fivonacci(n)
print(answer)