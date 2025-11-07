import csv
import os
from typing import Dict, List

from rich.console import Console
from rich.table import Table

console = Console()

#  Carpeta y archivo de datos
CARPETA_DATOS = "data"
ARCHIVO_CSV = os.path.join(CARPETA_DATOS, "estudiantes.csv")

# Crear la carpeta automáticamente si no existe
os.makedirs(CARPETA_DATOS, exist_ok=True)

# Crear el archivo CSV con encabezados si no existe
if not os.path.exists(ARCHIVO_CSV):
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "edad", "calificación"])


#  FUNCIONES PRINCIPALES

def agregar_estudiante(nombre: str, edad: int, calificacion: float) -> None:
    """Agrega un estudiante al archivo CSV.

    Si el archivo no existe, se crea con los encabezados.

    Args:
        nombre (str): Nombre del estudiante.
        edad (int): Edad del estudiante.
        calificacion (float): Calificación del estudiante.
    """
    with open(ARCHIVO_CSV, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, edad, calificacion])


def analizar_csv(columna: str) -> Dict[str, float]:
    """Analiza el archivo CSV y calcula estadísticas sobre una columna numérica.

    Args:
        columna (str): Columna a analizar ('edad' o 'calificación').

    Returns:
        dict[str, float]: Diccionario con promedio, máximo y mínimo.
    """
    valores: List[float] = []

    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    valor = float(fila[columna])
                    valores.append(valor)
                except (KeyError, ValueError):
                    continue
    except FileNotFoundError:
        console.print("[red]El archivo de estudiantes no existe todavía.[/red]")
        return {}

    if not valores:
        console.print("[yellow]No se encontraron datos válidos para analizar.[/yellow]")
        return {}

    promedio = sum(valores) / len(valores)
    maximo = max(valores)
    minimo = min(valores)

    return {"promedio": promedio, "maximo": maximo, "minimo": minimo}


def mostrar_resultados(resultados: Dict[str, float]) -> None:
    """Muestra los resultados del análisis en una tabla formateada con rich."""
    if not resultados:
        return

    tabla = Table(title="Resultados del Análisis")
    tabla.add_column("Métrica", style="cyan", justify="center")
    tabla.add_column("Valor", style="magenta", justify="center")

    for clave, valor in resultados.items():
        tabla.add_row(clave.capitalize(), f"{valor:.2f}")

    console.print(tabla)



# MENÚ PRINCIPAL

def main() -> None:
    """Función principal que gestiona el menú de la aplicación."""
    while True:
        console.print(
            "\n[bold green] Analizador de notas de estudiantes - "
            "Estudiantes[/bold green]"
        )
        console.print("1. Agregar estudiante")
        console.print("2. Analizar columna 'edad'")
        console.print("3. Analizar columna 'calificación'")
        console.print("4. Salir")

        opcion = console.input("[cyan]Selecciona una opción:[/cyan] ").strip()

        if opcion == "1":
            nombre = console.input("Nombre del estudiante: ").strip()
            try:
                edad = int(console.input("Edad: ").strip())
                calificacion = float(console.input("Calificación: ").strip())
            except ValueError:
                console.print(
                    "[red] Ingresa valores numéricos válidos para edad y "
                    "calificación.[/red]"
                )
                continue

            agregar_estudiante(nombre, edad, calificacion)
            console.print("[green] Estudiante agregado correctamente.[/green]")

        elif opcion == "2":
            resultados = analizar_csv("edad")
            mostrar_resultados(resultados)

        elif opcion == "3":
            resultados = analizar_csv("calificación")
            mostrar_resultados(resultados)

        elif opcion == "4":
            console.print("[bold red]👋 Saliendo del programa...[/bold red]")
            break

        else:
            console.print("[red]Opción inválida. Intenta de nuevo.[/red]")


if __name__ == "__main__":
    main()
