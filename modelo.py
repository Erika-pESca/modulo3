# -- coding: utf-8 --
"""
Módulo de datos simulado.
Contiene funciones de ejemplo para registrar o autenticar autores.
"""

# Simulación de base de datos
AUTORES = []

def crear_autor(nombre, email):
    autor = {"id_autor": len(AUTORES) + 1, "nombre_autor": nombre, "email": email}
    AUTORES.append(autor)
    return autor

def autenticar_autor(email, password):
    # En un sistema real, aquí validarías password_hash, etc.
    for a in AUTORES:
        if a["email"] == email:
            return a
    return None
