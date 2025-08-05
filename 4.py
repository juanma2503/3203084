def sumar(a, b):
    resultado = a + b
    return resultado

multipicador = lambda x, y: x*y

num1 = 7
num2 = 4

print("suma usando  funcion normal:", sumar(num1, num2))
print("multiplicación usando función lambda:", multipicador(num1, num2))