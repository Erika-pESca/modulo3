from typing import List

from rich.console import Console
from rich.table import Table

ARCHIVO_TAREAS = "tareas.txt"
console = Console()


def agregar_tarea(tarea: str) -> None:
    """Agrega una tarea al archivo de texto.

    Args:
        tarea (str): Descripción de la tarea a agregar.
    """
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea.strip() + "\n")


def ver_tareas() -> List[str]:
    """Lee y devuelve todas las tareas guardadas.

    Returns:
        list[str]: Lista con las tareas almacenadas.
    """
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
    except FileNotFoundError:
        tareas = []
    return tareas


def mostrar_tareas(tareas: List[str]) -> None:
    """Muestra las tareas en una tabla con formato usando rich.

    Args:
        tareas (list[str]): Lista de tareas a mostrar.
    """
    tabla = Table(title="Lista de Tareas")
    tabla.add_column("N°", style="cyan", justify="center")
    tabla.add_column("Tarea", style="magenta")

    if not tareas:
        console.print("[yellow]No hay tareas registradas.[/yellow]")
    else:
        for i, tarea in enumerate(tareas, start=1):
            tabla.add_row(str(i), tarea)
        console.print(tabla)


def main() -> None:
    """Función principal que gestiona el menú de la aplicación."""
    while True:
        console.print("\n[bold green]Gestor de Tareas[/bold green]")
        console.print("1. Agregar tarea")
        console.print("2. Ver tareas")
        console.print("3. Salir")

        opcion = console.input("[cyan]Selecciona una opción:[/cyan] ")

        if opcion == "1":
            tarea = console.input("Escribe la nueva tarea: ")
            agregar_tarea(tarea)
            console.print("[green]Tarea agregada correctamente![/green]")
        elif opcion == "2":
            mostrar_tareas(ver_tareas())
        elif opcion == "3":
            console.print("[bold red]¡Hasta pronto![/bold red]")
            break
        else:
            console.print("[red]Opción inválida, intenta de nuevo.[/red]")


if __name__ == "__main__":
    main()
