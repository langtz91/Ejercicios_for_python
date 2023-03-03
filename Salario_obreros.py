n = int(input("Ingrese número de obreros: "))

for i in range(1, n+1):
  horas_laboradas = int(input(f"Ingrese horas laboradas del trabajador {i}: "))

  if horas_laboradas <= 40:
     salario = 20 * horas_laboradas

  else:
     salario= 20 * 40 + 25 *  (horas_laboradas - 40)
     
  print (f"Su salario es $USD {salario}")