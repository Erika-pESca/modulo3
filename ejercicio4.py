import re
from typing import Any, Callable, List

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

# Instancia global de consola
console = Console()

def es_email_valido(email: str) -> bool:
    """
    Valida si un string tiene el formato básico de un email.
    """
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_regex.match(email))


MIN_NUMBER_VALIDATION = 10

def es_mayor_a_10(numero: int) -> bool:
    """
    Valida si un valor es un entero y es estrictamente mayor que 10.
    """
    if isinstance(numero, int):
        return numero > MIN_NUMBER_VALIDATION
    return False


def aplicar_validador(datos: List[Any], validador: Callable[[Any], bool]) -> List[Any]:
    """
    Aplica una función validadora a cada elemento de una lista de datos.
    """
    elementos_validos = []
    for elemento in datos:
        try:
            if validador(elemento):
                elementos_validos.append(elemento)
        except Exception as e:
            console.print(
                f"[bold yellow]⚠ Error de validación para '{elemento}': "
                f"{e}[/bold yellow]",
                style="yellow"
            )
            continue
    return elementos_validos


def obtener_datos_usuario(mensaje: str) -> List[str]:
    """
    Pide una lista de elementos al usuario y maneja errores de entrada vacía.
    """
    while True:
        entrada = Prompt.ask(f"[cyan]{mensaje}[/cyan]\n(Separados por comas)")
        if not entrada.strip():
            console.print(
                "[bold red]Error: Lista vacía. Intente de nuevo.\n",
                style="red"
            )
            continue
        return [item.strip() for item in entrada.split(',')]


def intentar_convertir_a_int(lista_str: List[str]) -> List[Any]:
    """
    Intenta convertir una lista de strings a enteros.
    """
    lista_convertida = []
    for item in lista_str:
        try:
            lista_convertida.append(int(item))
        except ValueError:
            lista_convertida.append(item)
    return lista_convertida


def mostrar_tabla(titulo: str, originales: List[Any], validos: List[Any]):
    """
    Muestra los datos originales y validados en una tabla bonita.
    """
    tabla = Table(title=titulo, title_style="bold magenta", show_lines=True)
    tabla.add_column("Dato Original", justify="center")
    tabla.add_column("¿Válido?", justify="center")

    for item in originales:
        es_valido = "Sí" if item in validos else " No"
        tabla.add_row(str(item), es_valido)

    console.print(tabla)


def main():
    console.print(Panel.fit(
        "[bold cyan]VALIDADOR GENÉRICO DE DATOS[/bold cyan]",
        style="bold blue"
    ))

    # --- PRUEBA 1: EMAILS ---
    console.print(Panel("PRUEBA 1: Validación de Emails", style="bold green"))
    email_strings = obtener_datos_usuario("Ingrese una lista de emails y otros strings")
    emails_validos = aplicar_validador(email_strings, es_email_valido)
    mostrar_tabla("Resultado Validación de Emails", email_strings, emails_validos)

    console.rule("[bold cyan]FIN DE PRUEBA 1[/bold cyan]")

    # --- PRUEBA 2: NÚMEROS MAYORES A 10 ---
    console.print(Panel(
        "PRUEBA 2: Validación de Números Mayores a 10",
        style="bold yellow"
    ))
    numeros_strings = obtener_datos_usuario(
        "Ingrese una lista de números (ej: 5, 12, 0, texto, 20)"
    )
    datos_convertidos = intentar_convertir_a_int(numeros_strings)
    numeros_mayores_a_10 = aplicar_validador(datos_convertidos, es_mayor_a_10)
    mostrar_tabla(
        "Resultado Validación de Números",
        numeros_strings,
        numeros_mayores_a_10
    )

    console.rule("[bold green]FIN DEL PROGRAMA[/bold green]")


if __name__ == "__main__":
    main()
