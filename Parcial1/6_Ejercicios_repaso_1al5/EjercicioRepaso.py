#Crear un programa que calcule y obtentga el total a pagar por un producto determi. Se debera solicitar el nombre y descripcion del producto,codigo, cantidad del producto,precio unitario. El total a pagar incluye el iva, y el descuento. Si se compran de 1 a5 productos se da el 10%, si es de 6 a 10 es el 15% de descuento y si son mas de 10 el 20% de descuento.


#informacion
Producto=input("Producto")
codrigo=input("codigo: ")
cantidad=int(input("caantidad: "))
preciou=float(input("presio unitario: "))

SubTotal=(cantidad*preciou)
iva=SubTotal*.16

if cantidad <=5:
    descuento=.90
elif cantidad >5 and cantidad <=10:
    descuento=.85
elif cantidad >10:
    descuento=.80

Total=(SubTotal+iva)*descuento

print(f"{Total}")
    
