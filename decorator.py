def decor(fun):
    def inner():
        n=fun()
        return n+10
    return inner
def num():
    return 5
res=decor(num)
print(res())
