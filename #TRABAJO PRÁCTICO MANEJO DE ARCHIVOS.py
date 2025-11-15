#TRABAJO PRÁCTICO MANEJO DE ARCHIVOS

#EJERCICIO 1
#Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad.
with open("productos.txt","w") as archivo:
    archivo.write("Pan,$1500,2\n")
    archivo.write("Huevos,$400,2\n")
    archivo.write("Botella de salsa,$500,2\n")

#EJERCICIO 2 
#Crear un programa que abra productos.txt, lea cada línea, la procese con strip() y .split(","), y muestre los productos 
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open("productos.txt","r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre}| Precio: {precio}| Cantidad: {cantidad}")

#EJERCICIO 3
#Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.
producto_nuevo=input("Ingrese un nuevo producto, precio, cantidad: ")
with open ("productos.txt","a") as archivo:
    archivo.write(producto_nuevo+"\n")
print("\nLista actualizada: ")
with open("productos.txt","r")as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre}| Precio: {precio}| Cantidad: {cantidad}")

#EJERCICO 4
#Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.
productos=[]
with open ("productos.txt","r") as archivo:
     for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto={
            "nombre":nombre,
            "precio":precio,
            "cantidad":cantidad
        }
        productos.append(producto)

for r in productos:
    print("\n",r)

#EJERCICIO 5
#Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.
buscar_producto=input("Ingrese el producto del que desea saber su información: ").strip().lower()
nombres=[p["nombre"].lower()for p in productos]
if buscar_producto in nombres:
    i=nombres.index(buscar_producto)
    producto=productos[i]
    print(f"Producto encontrado: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
else:
    print("Producto no encontrado.")

#EJERCICIO 6
#Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.
with open("producto.txt","w") as archivo:
    for p in productos:
        linea=f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)
with open("productos.txt","r")as archivo:
    contenido=archivo.read()
    print("\nContenido actualizado:")
    print("\n",contenido)