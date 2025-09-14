def buscar_palabra(palabra_buscada, *args):
    return "Palabra encontrada." if palabra_buscada in args else "Palabra no encontrada."


palabras=('gato','perro','chancho','conejo')
palabra = input("Ingrese la palabra a buscar: ")
resultado = buscar_palabra(palabra, *palabras)
print(resultado)


