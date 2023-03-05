limite = int(input("Ingrese el número límite: "))
x2 = 0
x3 = 1
print(x2)
print (x3)

for i in range(1, limite):
 x1 = x2
 x2 = x3 
 x3 = x1 + x2
 print(x3)
