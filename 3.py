try:
    # solicitar dos numeros al usuario
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    # intentar dividir los dos numeros
    resultado = num1 / num2 
    print(f"El resultado de la división es: {resultado}")
except ValueError:
    print("Por favor, ingrese solo números enteros.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Operación finalizada.")