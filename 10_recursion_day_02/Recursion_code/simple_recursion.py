def recursion(n):
    if n == 1:
        return 1
    return n + n**2

print(recursion(5))