# Ejercicio 1: Refactorización de Calculadora de IMC
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Crear el objeto de consola
console = Console()
valor=10
bajo_peso= 18.5
peso_normal =25
sobre_peso = 30
def pedir_dato(mensaje: str) -> float:
    """
    Pide al usuario los datos con  un número positivo con validación.
    """
    while True:
        try:
            valor = float(console.input(mensaje))
            if valor > 0:
                return valor
            else:
                console.print("[red]El valor debe ser mayor que cero.[/red]")
        except ValueError:
            console.print("[red]Por favor, ingrese un número válido.[/red]")


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el Índice de Masa Corporal (IMC).
    Detecta automáticamente si la altura está en centímetros y lo convierte en metros.
    """

    if altura > valor:
        altura = altura / 100  # Convertimos a metros

    imc = peso / (altura ** 2)
    return round(imc, 2)  # Redondea el resultado a dos decimales



def interpretar_imc(imc: float) -> str:
    """
    Interpreta el valor del IMC según los rangos estándar.
    """
    if imc < bajo_peso:
        return "Bajo peso"
    elif bajo_peso <= imc < peso_normal:
        return "Normal"
    elif peso_normal <= imc < sobre_peso:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main() -> None:
    """
    Controla el flujo del programa y muestra los resultados con formato Rich.
    """
    console.print(Panel.fit("[bold magenta] CALCULADORA DE IMC [/bold magenta]"))

    # Pedir datos validados
    peso = pedir_dato("[cyan]Ingrese su peso en kilogramos:[/cyan] ")
    altura = pedir_dato("[cyan]Ingrese su altura en metros:[/cyan] ")

    # Calcular e interpretar
    imc = calcular_imc(peso, altura)
    interpretacion = interpretar_imc(imc)

    # Crear tabla de resultados
    tabla = Table(
        title="[bold black on pink1]Resultado del IMC[/bold black on pink1]",
        title_style="yellow",
        border_style="blue"
    )
    tabla.add_column("Dato", style="bold cyan", justify="right")
    tabla.add_column("Valor", style="bold white")

    tabla.add_row("Peso (kg)", f"{peso}")
    tabla.add_row("Altura (m)", f"{altura}")
    tabla.add_row("IMC", f"{imc:.2f}")
    tabla.add_row("Interpretación", f"[bold magenta]{interpretacion}[/bold magenta]")

    # Mostrar resultado final
    console.print(
        Panel(
            tabla,
            title="[bold magenta]Resultado[/bold magenta]",
            border_style="magenta"
        )
    )


if __name__ == "__main__":
    main()
