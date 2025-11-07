"""
Ejercicio 6: Procesamiento de Datos con map y lambda
Dada una lista de diccionarios productos = [{"nombre": "Camisa", "precio": 50000}, ...],
utiliza la función map() junto con una función lambda para crear una nueva
lista que contenga solo los precios con un 10% de descuento aplicado.
"""

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Lista base de productos
productos = [
    {"nombre": "Camisa", "precio": 50000},
    {"nombre": "Pantalón", "precio": 80000},
    {"nombre": "Zapatos", "precio": 120000},
    {"nombre": "Corbata", "precio": 30000},
]


def calcular_precios_con_descuento(lista_productos: list[dict]) -> list[float]:
    """
    Aplica un 10% de descuento a una lista de productos usando map y lambda.
    """
    return list(map(lambda producto: producto["precio"] * 0.9, lista_productos))


def mostrar_tabla_productos(lista_productos: list[dict], precios_descuento: list[float]):
    """
    Muestra los productos con sus precios originales y con descuento en formato tabla.
    """
    tabla = Table(
        title=" Lista de Productos con Descuento",
        title_style="bold magenta",
        show_lines=True,
        box=box.ROUNDED,
    )

    tabla.add_column("Producto", justify="center", style="cyan", no_wrap=True)
    tabla.add_column("Precio Original", justify="center", style="bold yellow")
    tabla.add_column("Precio con Descuento", justify="center", style="bold green")

    for producto, nuevo_precio in zip(lista_productos, precios_descuento):
        tabla.add_row(
            producto["nombre"],
            f"${producto['precio']:,}",
            f"${nuevo_precio:,.2f}"
        )

    console.print(tabla)


def main():
    """
    Función principal para demostrar el uso de map y lambda con Rich.
    """
    console.print(Panel.fit(" [bold cyan]CÁLCULO DE DESCUENTOS CON MAP Y LAMBDA[/bold cyan]", style="bold blue"))

    # Cálculo con map + lambda
    precios_finales = calcular_precios_con_descuento(productos)

    # Mostrar resultados en tabla
    mostrar_tabla_productos(productos, precios_finales)

    console.print(Panel.fit(" [bold green]Descuentos aplicados correctamente[/bold green]", style="green"))


if __name__ == "__main__":
    main()
