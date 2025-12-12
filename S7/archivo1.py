# Estimación de esfuerzo bottom-up para testing
tareas = {
    "Analizar requisitos": 4,
    "Diseño de casos de prueba": 8,
    "Configurar entorno": 4,
    "Preparar datos de prueba": 3,
    "Ejecución de pruebas": 12,
    "Pruebas exploratorias": 6,
    "Reporte y gestión de defectos": 6,
    "Re-ejecución": 4
}

total_horas = sum(tareas.values())

print("ESTIMACIÓN DE ESFUERZO\n")
for tarea, horas in tareas.items():
    print(f"{tarea}: {horas} horas")

print("\nTotal estimado:", total_horas, "horas")
