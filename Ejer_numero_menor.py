cantidad_numeros = int(input("Cuál es la cantidad de números que desea ingresar: ")) 
menor = int(input("Ingrese número 1: "))

for i in range(2, cantidad_numeros+1):
  numero = int(input(f"Ingrese número {i}: "))
  
  if menor > numero:
    menor = numero
    
print (f"el número menor es {menor}")