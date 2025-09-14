def promedio(*args):
   # sum(args) realiza la autosuma de la lista -- len(args) cantidad de elementos de la lista
   # if de args devuelve true si contiene numeros y false cuando esta vacia
    return sum(args) / len(args) if args else "No se ingresaron números"


print(promedio(4,8,6,21,54,8,98,75,0))   # cuenta del promedio
print(promedio())          # "No se ingresaron números"
