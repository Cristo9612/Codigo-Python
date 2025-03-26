nombre = input("Nombre: ")
apellido = input("Apellido: ")
total_venta = float(input("Total de venta mensual: "))
nombre_completo = nombre + " " + apellido
porcentaje_comision = 13


print("Nombre del vendedor: " + nombre_completo)
print(f"Tu comision de este mes es: ${round(total_venta*porcentaje_comision/100,2)}")