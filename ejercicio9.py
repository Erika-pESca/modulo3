from functools import reduce

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

"""
Ejercicio 9: Sumatoria con reduce
1 Calcular la suma total de una lista de números [1, 2, 3, 4, 5].
2Concatenar una lista de strings ["Hola", " ", "SENA", "!"] en una sola frase.
"""

def calcular_suma_total(numeros: list[int | float]) -> int | float:
    """
    Calcula la suma total de una lista de números usando reduce.
    Retorna 0 si la lista está vacía.
    """
    if not numeros:
        return 0
    return reduce(lambda acc, el: acc + el, numeros)


def concatenar_strings(lista_strings: list[str]) -> str:
    """
    Concatena una lista de strings en una sola frase usando reduce.
    Retorna un string vacío si la lista está vacía.
    """
    if not lista_strings:
        return ""
    return reduce(lambda acc, el: acc + el, lista_strings)


def main():
    console.print(Panel.fit("[bold yellow]EJERCICIO 9: SUMATORIA CON REDUCE[/bold yellow]", border_style="green"))


    numeros = [1, 2, 3, 4, 5]
    suma_total = calcular_suma_total(numeros)

    tabla_numeros = Table(title="Cálculo de Suma Total", header_style="bold magenta")
    tabla_numeros.add_column("Lista de Números", justify="center", style="cyan")
    tabla_numeros.add_column("Suma Total", justify="center", style="green")

    tabla_numeros.add_row(str(numeros), str(suma_total))
    console.print(tabla_numeros)

    console.print("-" * 40)

    lista_strings = ["Hola", " ", "SENA", "!"]
    frase_concatenada = concatenar_strings(lista_strings)

    tabla_strings = Table(title="Concatenación de Strings", header_style="bold blue")
    tabla_strings.add_column("Lista de Strings", justify="center", style="cyan")
    tabla_strings.add_column("Frase Concatenada", justify="center", style="green")

    tabla_strings.add_row(str(lista_strings), f"'{frase_concatenada}'")
    console.print(tabla_strings)

    console.print(Panel.fit("[bold green] Operaciones completadas con éxito[/bold green]", border_style="blue"))


if __name__ == "__main__":
    main()
