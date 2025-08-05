print("Bucle FOR: ")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
    
print("Bucle WHILE: ")
contador = 0
while contador < 5:
    contador += 1
    if contador == 2:
        continue
    print(contador)
    if contador == 4:
        break