import os
import statistics
import random
import csv

trabajadores = ["Juan Perez", "María Garcia", "Carlos Lopez", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]


def asignar_sueldos():
    sueldos = {trabajador: random.randint(
        300000, 2500000) for trabajador in trabajadores}
    return sueldos


def clasificar_sueldos(sueldos):
    menores = {pe: su for pe, su in sueldos.items() if su < 800000}
    medianos = {pe: su for pe, su in sueldos.items() if 800000 <= su <= 2000000}
    superiores = {pe: su for pe, su in sueldos.items() if su > 2000000}

    print("Sueldos menores a $800.000")
    for trabajador, sueldo in menores.items():
        print(f"Nombre empleado:\t {trabajador}:\tSueldo ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000")
    for trabajador, sueldo in medianos.items():
        print(f"Nombre empleado:\t {trabajador}:\tSueldo ${sueldo}")

    print("\nSueldos superiores a $2.000.000")
    for trabajador, sueldo in superiores.items():
        print(f"Nombre empleado:\t {trabajador}:\tSueldo ${sueldo}")


def ver_estadisticas(sueldos):
    sueldos_list = list(sueldos.values())
    max_sueldo = max(sueldos_list)
    min_sueldo = min(sueldos_list)
    promedio_sueldo = statistics.mean(sueldos_list)

    if all(sueldo > 0 for sueldo in sueldos_list):
        media_geometrica = statistics.geometric_mean(sueldos_list)
        print(f"Media geometrica de sueldos: ${media_geometrica}")
    else:
        print("No se puede calcular la media geometrica debido a valores negativos.")

    print(f"\tSueldo mas alto: ${max_sueldo}")
    print(f"\tSueldo mas bajo: ${min_sueldo}")
    print(f"\tPromedio de sueldos: ${promedio_sueldo}")


def reporte_sueldos(sueldos):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'Reporte_De_Sueldos.csv')

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base",
                        "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for trabajador, sueldo in sueldos.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow(
                [trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])

    print(f"Reporte de sueldos generado satisfactoriamente en: '{file_path}'")


def menu():
    sueldos = asignar_sueldos()
    while True:
        print("\t\tBienvenido al Menu de Clasificación y Reporte de Sueldos\t\t")
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione la opcion que desea: ")

        if opcion == '1':
            sueldos = asignar_sueldos()
            print("Sueldos asignados aleatoreamente satisfactoreamente.")
        elif opcion == '2':
            clasificar_sueldos(sueldos)
        elif opcion == '3':
            ver_estadisticas(sueldos)
        elif opcion == '4':
            reporte_sueldos(sueldos)
        elif opcion == '5':
            print("Finalizando programa...")
            print("Desarrollado por Abraham Lopez")
            print("RUT 19.377.025-8")
            break
        else:
            print("\t\tParece que se ha equivocado de selección :(")
            print("\t\t¡Por favor Intente Nuevamente!")


if __name__ == "__main__":
    menu()
