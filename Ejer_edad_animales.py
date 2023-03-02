animal = input("Ingrese animal a estudiar: ")
if animal == "elefante":
  n = 5
elif animal == "jirafa":
  n = 7
elif animal == "chimpances":
  n = 8
conteo_menor = 0
conteo_mayor = 0
for i in range(1, n+1):
  edad = int(input(f"Ingrese la edad de el/la {animal} {i}: ")) 
  if edad < 5:
    conteo_menor += 1
  else: 
    conteo_mayor += 1
print(f"{animal} menores de 5 años: {conteo_menor}")
print(f"{animal} iguales o mayores a 5 años: {conteo_mayor}")