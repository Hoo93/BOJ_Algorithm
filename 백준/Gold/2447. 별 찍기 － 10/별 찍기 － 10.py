import sys

def fractal(n):
    if n ==3:
        return ["***","* *","***"]
    else:
        return make_fractal(fractal(n//3))

def make_fractal(a:list)->list:
    length = len(a)
    fractal_list = []
    for i in a:
        fractal_list.append(i*3)
    
    for i in a:
        fractal_list.append(i+" "*length+i)
    
    for i in a:
        fractal_list.append(i*3)

    return fractal_list

print("\n".join(fractal(int(sys.stdin.readline().rstrip()))))
