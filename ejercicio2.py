n = int(input("Ingrese el número de atletas finalistas: "))
atletas = {}

# Pidiendo los nombres y las marcas de los atletas
for i in range(n):
    nombre = input("Ingrese el nombre del atleta finalista: ")
    marca = float(input("Ingrese la marca del salto en metros: "))
    atletas[nombre] = marca

# Encontrando la atleta campeona
campeona = max(atletas, key=atletas.get)
marca_campeona = atletas[campeona]

# Verificando si se rompió el récord
if marca_campeona > 15.50:
    print(f"{campeona} ha ganado la medalla de oro y ha roto el récord con una marca de {marca_campeona} metros. Recibirá un pago de 500 millones.")
else:
    print(f"{campeona} ha ganado la medalla de oro con una marca de {marca_campeona} metros.")
