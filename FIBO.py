def f(n,k=1):
    if n<=2:
        return 1
    else:
        return f(n-1,k)+f(n-2,k)*k
print f(21)