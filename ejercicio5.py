"""
Ejercicio 5: Calculadora de Impuestos con Scope Global
Simula el cálculo de impuestos donde la tasa puede cambiar.
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

# Instancia de consola
console = Console()

# 1. Define una variable global TASA_IVA = 0.19.
TASA_IVA = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el IVA según la tasa global actual.
    """
    return precio_base * TASA_IVA


def actualizar_tasa_iva(nueva_tasa: float):
    """
    Actualiza la tasa global de IVA.
    """
    global TASA_IVA
    TASA_IVA = nueva_tasa


def mostrar_resultado(precio: float):
    """
    Muestra el cálculo de IVA actual en formato tabla.
    """
    iva = calcular_iva(precio)
    total = precio + iva

    tabla = Table(title=" Cálculo de IVA", title_style="bold magenta", show_lines=True)
    tabla.add_column("Concepto", justify="center", style="cyan")
    tabla.add_column("Valor", justify="center", style="bold yellow")

    tabla.add_row("Precio Base", f"${precio:,.2f}")
    tabla.add_row(f"Tasa IVA ({TASA_IVA*100:.0f}%)", f"${iva:,.2f}")
    tabla.add_row("Precio Total", f"${total:,.2f}")

    console.print(tabla)


def main():
    console.print(Panel.fit(
        " [bold cyan]CALCULADORA DE IMPUESTOS (Scope Global)[/bold cyan]",
        style="bold blue"
    ))

    # Paso 1: Mostrar cálculo inicial
    precio = float(Prompt.ask(
        "[green]Ingrese el precio base del producto[/green]",
        default="100"
    ))
    console.rule("[bold yellow]IVA Inicial[/bold yellow]")
    mostrar_resultado(precio)

    # Paso 2: Actualizar tasa de IVA
    nueva_tasa = float(Prompt.ask(
        "[cyan]Ingrese nueva tasa de IVA (por ejemplo 0.21 para 21%)[/cyan]",
        default="0.21"
    ))
    actualizar_tasa_iva(nueva_tasa)

    console.print(Panel(
        f" Tasa de IVA actualizada a [bold green]{TASA_IVA*100:.0f}%[/bold green]",
        style="green"
    ))

    # Paso 3: Mostrar nuevo cálculo
    console.rule("[bold yellow]Nuevo Cálculo con Tasa Actualizada[/bold yellow]")
    mostrar_resultado(precio)

    console.rule("[bold green]FIN DEL PROGRAMA[/bold green]")


if __name__ == "__main__":
    main()
