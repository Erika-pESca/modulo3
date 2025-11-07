from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def crear_contador():
    """
     Función Fábrica: Crea y retorna una nueva función de contador (closure).
    Inicializa 'conteo' en 0 y define y retorna la función 'incrementar'.
    """
    conteo = 0

    def incrementar():
        """
         Función Interna (El Contador): Modifica y retorna el conteo.
        Usa 'nonlocal' para acceder al conteo de la función externa.
        """
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def main():
    """
     Función principal para probar la independencia de los contadores.
    """
    console.print(Panel.fit(
        " [bold cyan]PRUEBA DE CONTADORES INDEPENDIENTES[/bold cyan]",
        border_style="bright_blue"
    ))

    # Crear los contadores
    contador_a = crear_contador()
    contador_b = crear_contador()

    console.print("\n[green] Contador A creado.[/green]")
    console.print("[green] Contador B creado.[/green]\n")

    # Crear tabla de resultados
    tabla = Table(
        title="Resultados de los Contadores",
        show_lines=True,
        header_style="bold magenta"
    )
    tabla.add_column("Acción", justify="center", style="cyan")
    tabla.add_column("Contador", justify="center", style="yellow")
    tabla.add_column("Resultado", justify="center", style="bold green")

    # Pruebas con los contadores
    tabla.add_row("Primer uso", "A", str(contador_a()))
    tabla.add_row("Segundo uso", "A", str(contador_a()))
    tabla.add_row("Primer uso", "B", str(contador_b()))
    tabla.add_row("Tercer uso", "A", str(contador_a()))

    console.print(tabla)

    console.print(Panel.fit(
        "[bold green]Cada contador mantiene su propio estado de forma "
        "independiente.[/bold green]",
        border_style="green"
    ))


if __name__ == "__main__":
    main()
