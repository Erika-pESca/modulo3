import json
import os
from typing import Dict, List

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

#  Carpeta y archivo del inventario
CARPETA_DATOS = "data"
ARCHIVO_INVENTARIO = os.path.join(CARPETA_DATOS, "inventario.json")

#  Crear la carpeta si no existe
os.makedirs(CARPETA_DATOS, exist_ok=True)

#  Crear el archivo JSON vacío si no existe
if not os.path.exists(ARCHIVO_INVENTARIO):
    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4, ensure_ascii=False)


# 📦 FUNCIONES DE PERSISTENCIA

def cargar_inventario() -> List[Dict]:
    """
    Carga el inventario desde el archivo JSON.
    Si el archivo no existe o está dañado, retorna una lista vacía.
    """
    try:
        with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        console.print(
            "[red]Error al leer el archivo JSON. Se inicializará vacío.[/red]"
        )
        return []


def guardar_inventario(inventario: List[Dict]) -> None:
    """
    Guarda el inventario en el archivo JSON.
    """
    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as file:
        json.dump(inventario, file, indent=4, ensure_ascii=False)



# 📦 FUNCIONES DEL INVENTARIO

def agregar_producto(inventario: List[Dict]) -> None:
    """
    Agrega un nuevo producto al inventario con validaciones.
    """
    console.print(
        Panel("[bold yellow] Agregar Nuevo Producto[/bold yellow]", expand=False)
    )

    nombre = console.input("[cyan]Nombre del producto:[/cyan] ").strip()
    if not nombre:
        console.print("[red] El nombre no puede estar vacío.[/red]")
        return

    try:
        cantidad = int(console.input("[cyan]Cantidad en stock:[/cyan] ").strip())
        if cantidad < 0:
            console.print("[red]La cantidad no puede ser negativa.[/red]")
            return
        precio = float(console.input("[cyan]Precio por unidad:[/cyan] ").strip())
        if precio <= 0:
            console.print("[red]El precio debe ser mayor a 0.[/red]")
            return
    except ValueError:
        console.print("[red]Ingrese valores numéricos válidos.[/red]")
        return

    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    guardar_inventario(inventario)
    console.print("[green]Producto agregado correctamente.[/green]")


def vender_producto(inventario: List[Dict]) -> None:
    """
    Permite vender (disminuir) la cantidad de un producto existente.
    """
    console.print(Panel("[bold yellow]Registrar Venta[/bold yellow]", expand=False))

    nombre = console.input("[cyan]Nombre del producto a vender:[/cyan] ").strip()

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            try:
                cantidad_vendida = int(console.input(
                    "[cyan]Cantidad vendida:[/cyan] ").strip())

                if cantidad_vendida <= 0:
                    console.print("[red] La cantidad debe ser mayor a 0.[/red]")
                    return
                if cantidad_vendida > producto["cantidad"]:
                    console.print("[red] No hay suficiente stock disponible.[/red]")
                    return

                producto["cantidad"] -= cantidad_vendida
                guardar_inventario(inventario)
                console.print(
                    f"[green]Venta registrada. Stock restante: "
                    f"{producto['cantidad']}[/green]"
                )
                return
            except ValueError:
                console.print("[red]Ingrese una cantidad válida.[/red]")
                return

    console.print("[red] Producto no encontrado en el inventario.[/red]")


def mostrar_inventario(inventario: List[Dict]) -> None:
    """
    Muestra el inventario completo en una tabla con Rich.
    """
    console.print(Panel("[bold magenta]INVENTARIO ACTUAL[/bold magenta]", expand=False))

    if not inventario:
        console.print("[red]El inventario está vacío.[/red]")
        return

    tabla = Table(title="Inventario de Productos")
    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Cantidad", style="green", justify="center")
    tabla.add_column("Precio (💲)", style="yellow", justify="center")
    tabla.add_column("Valor Total", style="bold magenta", justify="center")

    total_general = 0

    for producto in inventario:
        valor_total = producto["cantidad"] * producto["precio"]
        total_general += valor_total
        tabla.add_row(
            producto["nombre"],
            str(producto["cantidad"]),
            f"${producto['precio']:.2f}",
            f"${valor_total:.2f}"
        )

    console.print(tabla)
    console.print(
        f"[bold cyan] Valor total del inventario: ${total_general:.2f}[/bold cyan]"
    )



#  MENÚ PRINCIPAL

def main() -> None:
    """
    Función principal del programa.
    Permite gestionar el inventario mediante un menú interactivo.
    """
    inventario = cargar_inventario()

    while True:
        console.print(
            Panel("[bold blue]=== GESTOR DE INVENTARIO PERSISTENTE ===[/bold blue]")
        )
        console.print("1 Agregar producto")
        console.print("2 Vender producto")
        console.print("3 Mostrar inventario")
        console.print("4 Salir\n")

        opcion = console.input(
            "[yellow]Seleccione una opción (1-4): [/yellow] ").strip()

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            vender_producto(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            console.print("[green] Saliendo del sistema...[/green]")
            break
        else:
            console.print("[red] Opción inválida. Intente nuevamente.[/red]")


if __name__ == "__main__":
    main()
