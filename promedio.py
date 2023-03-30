def ejercicio_promedio(estudiantes):
    promedios_mujeres = []
    promedios_hombres = []
    promedios_fp = []
    promedios_pp = []
    promedios_n = []
    promedios_d = []
    for estudiante in estudiantes.values():
        promedio = estudiante["promedio_acumulado"]
        sexo = estudiante["sexo"]
        situacion = estudiante["situacion"]

        if sexo == "M":
            promedios_hombres.append(promedio)
        else:
            promedios_mujeres.append(promedio)

        if situacion == "FP":
            promedios_fp.append(promedio)
        elif situacion == "PP":
            promedios_pp.append(promedio)
        elif situacion == "N":
            promedios_n.append(promedio)
        elif situacion == "D":
            promedios_d.append(promedio)

    promedios_por_sexo = [("Mujeres", promedios_mujeres), ("Hombres", promedios_hombres)]
    promedios_por_situacion = [("FP", promedios_fp), ("PP", promedios_pp), ("N", promedios_n), ("D", promedios_d)]
    promedios = {"promedios": promedios_por_sexo + promedios_por_situacion}

    if promedios_mujeres:
        promedios["promedio_mujeres"] = sum(promedios_mujeres) / len(promedios_mujeres)
    if promedios_hombres:
        promedios["promedio_hombres"] = sum(promedios_hombres) / len(promedios_hombres)
    if promedios_fp:
        promedios["promedio_fp"] = sum(promedios_fp) / len(promedios_fp)
    if promedios_pp:
        promedios["promedio_pp"] = sum(promedios_pp) / len(promedios_pp)
    if promedios_n:
        promedios["promedio_n"] = sum(promedios_n) / len(promedios_n)
    if promedios_d:
        promedios["promedio_d"] = sum(promedios_d) / len(promedios_d)

    promedios_todos = promedios_mujeres + promedios_hombres + promedios_fp + promedios_pp + promedios_n + promedios_d
    promedios["máximo"] = max(promedios_todos)
    promedios["mínimo"] = min(promedios_todos)
    return promedios
num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
estudiantes = {}
for i in range(num_estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    promedio = float(input(f"Ingrese el promedio acumulado de {nombre}: "))
    sexo = input(f"Ingrese el sexo de {nombre} (M/F): ")
    situacion = input(f"Ingrese la situación de {nombre} (FP/PP/N/D): ")
    estudiantes[nombre] = {"promedio_acumulado": promedio, "sexo": sexo, "situacion": situacion}
resultados = ejercicio_promedio(estudiantes)
print("sus Resultados son:", estudiantes)
