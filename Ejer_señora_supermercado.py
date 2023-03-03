cantidad_productos = int(input("Ingrese cantidad de productos a comprar: "))

total_compra = 0

for i in range(1, cantidad_productos +1):
  
 articulo = input(f"Ingrese nombre de articulo {i}: " )
    
 cantidad_articulo = int(input("Ingrese la cantidad del articulo: "))
    
 precio_articulo = int(input("Ingrese precio del artículo: " ))

 total = cantidad_articulo * precio_articulo

 total_compra = total_compra + total
    
 print(f"{cantidad_articulo} * $ {precio_articulo} = $ {total}") 

print(f" Total compra = $ {total_compra}")