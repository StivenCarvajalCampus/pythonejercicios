km_totales = 3277  # Total de kilómetros por recorrer durante toda la vuelta
km_lider = int(input("Ingrese el número de kilómetros recorridos con la camiseta de líder: "))
km_restantes = km_totales - km_lider  # Kilómetros restantes a recorrer sin la camiseta de líder

sueldo_km = float(input("Ingrese el sueldo básico por kilómetro recorrido: "))
valor_pagar = km_lider * sueldo_km  # Valor a pagar por kilómetros recorridos con la camiseta de líder

if km_lider > 1800:
    km_especiales = km_lider - 1800
    valor_pagar_especiales = km_especiales * sueldo_km * 1.25  # Valor a pagar por kilómetros especiales
    valor_pagar += valor_pagar_especiales

valor_pagar += km_restantes * sueldo_km  # Valor a pagar por kilómetros restantes sin la camiseta de líder

print(f"\nEl valor a pagar total es: ${valor_pagar:.2f}")
