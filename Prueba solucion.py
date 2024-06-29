import random
import math

# Función para registrar un producto en la lista de productos
def registrar_producto(productos):
    try:
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = random.uniform(10, 1000)

        # Crear un diccionario para el producto
        producto = {
            "nombre": nombre,
            "categoria": categoria,
            "cantidad": cantidad,
            "precio": precio
        }

        # Agregar el diccionario del producto a la lista de productos
        productos.append(producto)
        print("Producto registrado exitosamente!")
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")

# Función para listar todos los productos
def listar_productos(productos):
    if productos:
        for producto in productos:
            print(f'Nombre: {producto["nombre"]}, Categoría: {producto["categoria"]}, Cantidad: {producto["cantidad"]}, Precio: {producto["precio"]:.2f}')
    else:
        print("No hay productos registrados.")

# Función para buscar productos por categoría
def buscar_por_categoria(productos):
    categoria = input("Ingrese la categoría que desea buscar: ")
    encontrados = [producto for producto in productos if producto["categoria"].lower() == categoria.lower()]
    
    if encontrados:
        for producto in encontrados:
            print(f'Nombre: {producto["nombre"]}, Cantidad: {producto["cantidad"]}, Precio: {producto["precio"]:.2f}')
    else:
        print("No se encontraron productos en esta categoría.")

# Función para calcular el precio promedio de los productos
def calcular_promedio(productos):
    precios = [producto["precio"] for producto in productos]
    if precios:
        promedio = math.fsum(precios) / len(precios)
        print(f'El precio promedio de todos los productos es: {promedio:.2f}')
    else:
        print("No hay precios registrados para calcular el promedio.")

# Función para guardar la lista de productos en un archivo de texto
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f'{producto}\n')
    print("Lista de productos guardada exitosamente en productos.txt")

# Función principal del programa
def main():
    productos = []
    
    while True:
        print("1. Registrar producto")
        print("2. Listar todos los productos")
        print("3. Buscar productos por categoría")
        print("4. Calcular el precio promedio de los productos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            listar_productos(productos)
        elif opcion == "3":
            buscar_por_categoria(productos)
        elif opcion == "4":
            calcular_promedio(productos)
        elif opcion == "5":
            guardar_productos(productos)
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
