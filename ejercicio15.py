import json
from typing import Dict, List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# ========================================================
# 🔹 FUNCIONES DE PERSISTENCIA
# ========================================================
def cargar_biblioteca(nombre_archivo: str) -> List[Dict[str, Optional[str]]]:
    """
    Carga los datos de la biblioteca desde un archivo JSON.
    Si el archivo no existe o está vacío, devuelve una lista vacía.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_biblioteca(
    nombre_archivo: str, datos: List[Dict[str, Optional[str]]]
) -> None:
    """
    Guarda el estado actual de la biblioteca en el archivo JSON.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)


# ========================================================
# 🔹 FUNCIONES PRINCIPALES DE LÓGICA
# ========================================================
def prestar_libro(
    libros: List[Dict[str, Optional[str]]], libro_id: str, nombre_aprendiz: str
) -> bool:
    """
    Marca un libro como prestado a un aprendiz.
    """
    for libro in libros:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"]:
                console.print("[red]El libro ya está prestado.[/red]")
                return False
            libro["prestado_a"] = nombre_aprendiz
            console.print(
                f"[green] Libro '{libro['titulo']}' prestado a "
                f"{nombre_aprendiz}.[/green]"
            )
            return True
    console.print("[red]No se encontró el libro con ese ID.[/red]")
    return False


def devolver_libro(libros: List[Dict[str, Optional[str]]], libro_id: str) -> bool:
    """
    Marca un libro como devuelto (prestado_a = None).
    """
    for libro in libros:
        if libro["libro_id"] == libro_id:
            if libro["prestado_a"] is None:
                console.print(
                    "[yellow]Ese libro no está prestado actualmente.[/yellow]"
                )
                return False
            libro["prestado_a"] = None
            console.print(
                f"[green]Libro '{libro['titulo']}' devuelto correctamente.[/green]"
            )
            return True
    console.print("[red] Libro no encontrado.[/red]")
    return False


def buscar_libro(
    libros: List[Dict[str, Optional[str]]], query: str
) -> List[Dict[str, Optional[str]]]:
    """
    Busca libros cuyo título contenga el texto especificado.
    """
    resultados = [libro for libro in libros if query.lower() in libro["titulo"].lower()]
    mostrar_tabla(resultados, f"Resultados de búsqueda para '{query}'")
    return resultados


def ver_libros_prestados(
    libros: List[Dict[str, Optional[str]]]
) -> List[Dict[str, Optional[str]]]:
    """
    Muestra los libros que están actualmente prestados.
    """
    prestados = [libro for libro in libros if libro["prestado_a"]]
    mostrar_tabla(prestados, " Libros Prestados")
    return prestados


# ========================================================
# 🔹 FUNCIÓN DE VISUALIZACIÓN CON RICH
# ========================================================
def mostrar_tabla(libros: List[Dict[str, Optional[str]]], titulo: str) -> None:
    """
    Muestra una tabla bonita con los libros.
    """
    tabla = Table(title=titulo, show_header=True, header_style="bold magenta")
    tabla.add_column("ID", justify="center", style="cyan")
    tabla.add_column("Título", justify="left", style="white")
    tabla.add_column("Prestado A", justify="center", style="green")

    if not libros:
        tabla.add_row("—", "No hay registros", "—")
    else:
        for libro in libros:
            tabla.add_row(
                libro["libro_id"], libro["titulo"], libro["prestado_a"] or "Disponible"
            )

    console.print(Panel.fit(tabla, border_style="blue"))


# ========================================================
# 🔹 FUNCIÓN PRINCIPAL
# ========================================================
def main():
    """
    Menú principal del sistema de biblioteca.
    """
    archivo = "biblioteca.json"
    libros = cargar_biblioteca(archivo)

    console.print(
        Panel.fit(
            " [bold yellow]SISTEMA DE BIBLIOTECA[/bold yellow]", border_style="green"
        )
    )

    while True:
        console.print("\n[cyan]Seleccione una opción:[/cyan]")
        console.print("1  Ver libros prestados")
        console.print("2  Buscar libro por título")
        console.print("3 Prestar libro")
        console.print("4  Devolver libro")
        console.print("5 Salir\n")

        opcion = console.input("[bold yellow]> [/bold yellow]").strip()

        if opcion == "1":
            ver_libros_prestados(libros)

        elif opcion == "2":
            query = console.input(
                "[cyan]Ingrese parte del título a buscar:[/cyan] "
            ).strip()
            buscar_libro(libros, query)

        elif opcion == "3":
            libro_id = console.input(
                "[cyan]Ingrese el ID del libro a prestar:[/cyan] "
            ).strip()
            nombre = console.input(
                "[cyan]Ingrese el nombre del aprendiz:[/cyan] "
            ).strip()
            if prestar_libro(libros, libro_id, nombre):
                guardar_biblioteca(archivo, libros)

        elif opcion == "4":
            libro_id = console.input(
                "[cyan]Ingrese el ID del libro a devolver:[/cyan] "
            ).strip()
            if devolver_libro(libros, libro_id):
                guardar_biblioteca(archivo, libros)

        elif opcion == "5":
            guardar_biblioteca(archivo, libros)
            console.print("[green] Gracias por usar el sistema de biblioteca.[/green]")
            break

        else:
            console.print("[red] Opción inválida, intente nuevamente.[/red]")


# ========================================================
# 🔹 PUNTO DE ENTRADA
# ========================================================
if __name__ == "__main__":
    main()
