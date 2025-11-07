"""
Ejercicio 7: Filtrado de Estudiantes con filter y lambda
Dada una lista de tuplas estudiantes = [("Ana", 4.5), ("Juan", 2.8), ("Maria", 3.9)],
usa filter() y una lambda para obtener una nueva lista que contenga únicamente
a los estudiantes que aprobaron (nota >= 3.0).
"""

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Lista base de estudiantes
estudiantes = [
    ("Ana", 4.5),
    ("Juan", 2.8),
    ("Maria", 3.9),
    ("Carlos", 2.9),
    ("Luisa", 3.0),
    ("Pedro", 5.0)
]


MIN_GRADE_APPROVED = 3.0

def filtrar_estudiantes_aprobados(lista_estudiantes: list[tuple]) -> list[tuple]:
    """
    Filtra una lista de estudiantes para obtener solo los que tienen una nota >= 3.0.
    Utiliza la función filter() y una expresión lambda.
    """
    return list(filter(lambda estudiante: estudiante[1] >= MIN_GRADE_APPROVED, lista_estudiantes))


def mostrar_tabla_estudiantes(lista_estudiantes: list[tuple], titulo: str, color_titulo: str):
    """
    Muestra una tabla formateada con Rich para visualizar estudiantes y notas.
    """
    tabla = Table(
        title=titulo,
        title_style=f"bold {color_titulo}",
        box=box.ROUNDED,
        show_lines=True
    )

    tabla.add_column("Nombre", justify="center", style="cyan", no_wrap=True)
    tabla.add_column("Nota", justify="center", style="yellow")

    for nombre, nota in lista_estudiantes:
        color_nota = "green" if nota >= MIN_GRADE_APPROVED else "red"
        tabla.add_row(nombre, f"[{color_nota}]{nota}[/]")

    console.print(tabla)


def main():
    """
    Función principal para demostrar el filtrado de estudiantes usando filter + lambda.
    """
    console.print(Panel.fit(" [bold cyan]FILTRADO DE ESTUDIANTES CON FILTER Y LAMBDA[/bold cyan]", style="bold blue"))
    # Mostrar lista completa
    mostrar_tabla_estudiantes(estudiantes, " Lista completa de estudiantes", "magenta")

    # Filtrar aprobados
    estudiantes_aprobados = filtrar_estudiantes_aprobados(estudiantes)

    # Mostrar lista filtrada
    mostrar_tabla_estudiantes(estudiantes_aprobados, " Estudiantes que aprobaron (nota >= 3.0)", "green")

    console.print(Panel.fit(" [bold green]Filtrado completado correctamente[/bold green]", style="green"))


if __name__ == "__main__":
    main()
