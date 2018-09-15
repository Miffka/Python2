#-*-coding:utf8;-*-
#qpy:3
#qpy:console

n, k = map(int, input().split())
def C(l, m):
    if m > l:
        return 0
    elif m == 0:
        return 1
    else:
        return C(l-1, m) + C(l-1, m-1)
print(C(n, k))