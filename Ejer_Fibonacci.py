limite = int(input("Ingrese el número límite: "))
x2 = 0
x3 = 1

for i in range(0, limite):
 x1 = x2
 x2 = x3 
 x3 = x1 + x2

 print(x1)
