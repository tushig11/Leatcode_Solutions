
f1 = lambda x: x*x
f2 = lambda x: x+x
func = [f1,f2]
arr = [1,2,3,4]

def cmap(funcs,arr):
    fs = iter(funcs)
    data = iter(arr)
    for f in fs:
        data = map(f,data);
    for d in data:
        print(d)

cmap(func,arr);
