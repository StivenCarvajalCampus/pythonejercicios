num_almacenes = 6
articulos = {}  # Diccionario para almacenar las ventas totales de cada articulo

# Inicializar el diccionario con valores en cero para cada articulo
for i in range(num_almacenes):
    for j in range(2):
        articulo = input(f"Ingrese el tipo de artículo vendido en el almacén {i+1}, registro {j+1}: ")
        unidades = int(input(f"Ingrese el número de unidades vendidas de {articulo} en el almacén {i+1}, registro {j+1}: "))
        articulos[articulo] = articulos.get(articulo, 0) + unidades

# Encontrar el articulo más vendido en general
articulo_mas_vendido = max(articulos, key=articulos.get)
print(f"\nEl artículo más vendido en general es {articulo_mas_vendido} con un total de {articulos[articulo_mas_vendido]} unidades vendidas.")

# Encontrar el almacén que más vendió
max_vendido = 0
max_almacen = 0

for i in range(num_almacenes):
    ventas_almacen = 0
    for j in range(5):
        articulo = input(f"Ingrese el tipo de artículo vendido en el almacén {i+1}, registro {j+1}: ")
        unidades = int(input(f"Ingrese el número de unidades vendidas de {articulo} en el almacén {i+1}, registro {j+1}: "))
        ventas_almacen += unidades
        articulos[articulo] += unidades
    
    if ventas_almacen > max_vendido:
        max_vendido = ventas_almacen
        max_almacen = i+1

# Encontrar el articulo más vendido en el almacén más vendido
articulos_almacen = {}
for j in range(5):
    articulo = input(f"Ingrese el tipo de artículo vendido en el almacén {max_almacen}, registro {j+1}: ")
    unidades = int(input(f"Ingrese el número de unidades vendidas de {articulo} en el almacén {max_almacen}, registro {j+1}: "))
    articulos_almacen[articulo] = articulos_almacen.get(articulo, 0) + unidades

articulo_mas_vendido_almacen = max(articulos_almacen, key=articulos_almacen.get)

print(f"\nEl almacén que más vendió fue el {max_almacen} con un total de {max_vendido} unidades vendidas.")
print(f"El artículo más vendido en el almacén {max_almacen} fue {articulo_mas_vendido_almacen} con un total de {articulos_almacen[articulo_mas_vendido_almacen]} unidades vendidas.")
