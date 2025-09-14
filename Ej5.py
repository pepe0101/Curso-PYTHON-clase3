def promedio(*args):
    if len(args) == 0:  # sin argumentos
        return "Error: no se pasaron números"
    elif len(args) == 1:  # solo uno
        return "Error: se necesita al menos 2 números para calcular un promedio"
    else:
        return sum(args) / len(args)


# Ejemplos de uso
print(promedio())            # Error: no se pasaron números
print(promedio(5))           # Error: se necesita al menos 2 números
print(promedio(5, 10, 15))   # 10.0
