import re

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

"""
Ejercicio 8: Transformación de Datos con List y Dictionary Comprehensions
Dado un texto largo como un string, realiza lo siguiente:
1. Usa una List Comprehension para crear una lista de todas las palabras del
texto que tengan más de 5 letras y estén en mayúsculas.
2. Usa una Dictionary Comprehension para crear un diccionario que cuente
la longitud de cada palabra de la lista resultante. {"PALABRA": 7, ...}.
"""

texto_largo = (
    "La programación funcional es un paradigma de programación declarativa "
    "basado en el uso de funciones matemáticas. El código escrito en este estilo "
    "tiende a ser más conciso, más predecible y más fácil de probar que el código imperativo."
)


MIN_WORD_LENGTH = 5

def transformar_texto(texto: str) -> tuple[list[str], dict[str, int]]:
    """
    Transforma un texto largo en:
    1. Una lista de palabras con más de 5 letras en mayúsculas.
    2. Un diccionario con la longitud de esas palabras.
    """
    # Limpiar puntuación con regex
    palabras_limpias = re.sub(r"[^\w\s]", "", texto).split()

    # List comprehension: palabras > 5 letras en mayúsculas
    palabras_filtradas = [p.upper() for p in palabras_limpias if len(p) > MIN_WORD_LENGTH]

    # Dictionary comprehension: longitud de cada palabra
    conteo_longitudes = {p: len(p) for p in palabras_filtradas}

    return palabras_filtradas, conteo_longitudes

    # Dictionary comprehension: longitud de cada palabra
    conteo_longitudes = {p: len(p) for p in palabras_filtradas}

    return palabras_filtradas, conteo_longitudes


def main():
    console.print(Panel.fit("[bold yellow]EJERCICIO 8: TRANSFORMACIÓN DE DATOS[/bold yellow]", border_style="green"))

    console.print("[cyan]Texto original:[/cyan]")
    console.print(f"[white]{texto_largo}[/white]\n")

    palabras, conteo = transformar_texto(texto_largo)

    # Mostrar palabras con Rich Table
    tabla_palabras = Table(title="Palabras con más de 5 letras", header_style="bold magenta")
    tabla_palabras.add_column("N°", justify="center", style="cyan")
    tabla_palabras.add_column("Palabra", justify="left", style="green")

    for i, palabra in enumerate(palabras, start=1):
        tabla_palabras.add_row(str(i), palabra)

    console.print(tabla_palabras)

    # Mostrar diccionario de longitudes
    tabla_conteo = Table(title="Longitud de las Palabras", header_style="bold blue")
    tabla_conteo.add_column("Palabra", justify="left", style="cyan")
    tabla_conteo.add_column("Longitud", justify="center", style="green")

    for palabra, longitud in conteo.items():
        tabla_conteo.add_row(palabra, str(longitud))

    console.print(tabla_conteo)

    console.print(Panel.fit("[bold green]Transformación completada correctamente[/bold green]", border_style="blue"))


if __name__ == "__main__":
    main()
