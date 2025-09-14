def promedio(*args):
    if len(args):
       promedio=sum(args)/len(args) 

    return promedio if args else "No hay números"

print(promedio(4,8,6))
print(promedio())