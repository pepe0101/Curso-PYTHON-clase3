def ingresar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def calcular_mayor(a, b):
    return a if a > b else b 


print("=== Comparador de dos números ===") 
num1 = ingresar_numero("Ingrese el primer número: ")
num2 = ingresar_numero("Ingrese el segundo número: ")   
mayor = calcular_mayor(num1, num2)
print(f"El número mayor es: {mayor}")

