def calcular_estadisticas():
    num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

    total_promedios = 0
    promedio_mujeres = 0
    promedio_hombres = 0
    mujeres = 0
    hombres = 0

    for i in range(num_estudiantes):
        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        promedio = float(input(f"Ingrese el promedio acumulado de {nombre}: "))
        sexo = input(f"Ingrese el sexo de {nombre} (M/F): ")
        total_promedios += promedio
        if sexo == "F":
            promedio_mujeres += promedio
            mujeres += 1
        else:
            promedio_hombres += promedio
            hombres += 1

    promedio_promedios = total_promedios / num_estudiantes

    if mujeres > 0:
        promedio_mujeres /= mujeres
    if hombres > 0:
        promedio_hombres /= hombres

    resultados = {
        "cantidad_estudiantes": num_estudiantes,
        "promedio_promedios": promedio_promedios,
        "promedio_mujeres": promedio_mujeres,
        "promedio_hombres": promedio_hombres
    }
    return resultados
resultados = calcular_estadisticas()
print("El promedio de los promedios es:", resultados["promedio_promedios"])
