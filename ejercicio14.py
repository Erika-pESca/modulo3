import csv
import json

from rich.console import Console
from rich.table import Table

console = Console()


def leer_csv(ruta_csv: str) -> list:
    """
    Lee los datos de estudiantes desde un archivo CSV.
    Retorna una lista de diccionarios con los datos.
    """
    estudiantes = []
    try:
        with open(ruta_csv, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                estudiantes.append(fila)
    except FileNotFoundError:
        console.print(f"[red]Error:[/red] No se encontró el archivo {ruta_csv}")
    return estudiantes


def leer_json(ruta_json: str) -> list:
    """
    Lee los datos de cursos desde un archivo JSON.
    Retorna una lista de diccionarios.
    """
    try:
        with open(ruta_json, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[red]Error:[/red] No se encontró el archivo {ruta_json}")
        return []


def generar_reporte(estudiantes: list, cursos: list, ruta_salida: str):
    """
    Combina los datos de estudiantes y cursos para generar un reporte.
    Muestra el reporte en la consola con Rich y lo guarda en un archivo TXT.
    """
    # Crear un diccionario donde cada estudiante tiene una lista de cursos
    relacion = {e["id"]: {"nombre": e["nombre"], "cursos": []} for e in estudiantes}

    # Asignar cursos a cada estudiante según el JSON
    for curso in cursos:
        for id_estudiante in curso.get("estudiantes", []):
            if id_estudiante in relacion:
                relacion[id_estudiante]["cursos"].append(curso["nombre"])

    # Crear tabla Rich para mostrar en consola
    table = Table(title="📘 Reporte de Cursos por Estudiante")
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Nombre", style="bold")
    table.add_column("Cursos inscritos", style="green")

    # Crear texto del reporte
    texto_reporte = " REPORTE DE CURSOS POR ESTUDIANTE\n\n"

    for id_est, datos in relacion.items():
        cursos_lista = ", ".join(datos["cursos"]) if datos["cursos"] else "Sin cursos"
        table.add_row(id_est, datos["nombre"], cursos_lista)
        texto_reporte += f"{datos['nombre']} ({id_est}) → {cursos_lista}\n"

    # Mostrar tabla en consola
    console.print(table)

    # Guardar reporte en archivo de texto
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(texto_reporte)

    console.print(
        f"\n[bold green]✅ Reporte generado correctamente en:[/bold green] "
        f"{ruta_salida}"
    )


# Ejemplo de ejecución directa
if __name__ == "__main__":
    estudiantes = leer_csv("estudiantes.csv")
    cursos = leer_json("cursos.json")
    generar_reporte(estudiantes, cursos, "reporte.txt")
