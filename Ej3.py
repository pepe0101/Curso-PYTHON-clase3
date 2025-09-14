def par_o_impar(*args):
    n = args[0]  # 0 es el primer dato de la lista.En este caso solo tiene un dato
    return "PAR" if n % 2 == 0 else "IMPAR"

numero = int(input("Ingrese un número: "))
print(f"El número {numero} es {par_o_impar(numero)}")
