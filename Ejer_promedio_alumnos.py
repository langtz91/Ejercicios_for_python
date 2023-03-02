n = int(input("Ingrese número de mujeres: "))
suma_edad_mujeres = 0
for i in range(1, n+1):
  edad_mujeres = int(input(f"Ingrese edad de las mujeres {i}: ")) 
  suma_edad_mujeres = suma_edad_mujeres + edad_mujeres
n1 = int(input("Ingrese número de hombres: "))
suma_edad_hombres = 0
for i in range(1, n1+1):
  edad_hombres = int(input(f"Ingrese edad de las hombres {i}: "))
  suma_edad_hombres = suma_edad_hombres + edad_hombres
promedio_mujeres = suma_edad_mujeres / n 
redondeo_mujeres = round(promedio_mujeres, 2)
promedio_hombres = suma_edad_hombres / n1
redondeo_hombres = round(promedio_hombres, 2)
promedio_alumnos = (suma_edad_mujeres + suma_edad_hombres) / (n + n1)
redondeo_alumnos = round(promedio_alumnos, 2)
print(f"el promedio de edad de las mujeres es {redondeo_mujeres} años")
print(f"el promedio de edad de los hombres es {redondeo_hombres} años")
print(f"el promedio de edad de los alumnos es {redondeo_alumnos} años")