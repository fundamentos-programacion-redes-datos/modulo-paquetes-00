"""
    Crear funciones en un módulo independiente llamado 'mis_funciones'.
"""

# Definición de la función para imprimir un reporte con los datos ingresados
def imprimir_reporte(nombre, apellido, edad, ciudad, correo):
    """
    Función que genera un reporte de "matrícula" a partir de los datos ingresados,
    aplicando transformaciones (pasarlos a mayúsculas, con la función upper) 
    a los valores de nombre, apellido y ciudad.
    """

    # Se construye la cadena formateada con la información del estudiante
    cadena = f"Reporte de Matrícula\n"\
             f"Nombre: {nombre.upper()}\n"\
             f"Apellido: {apellido.upper()}\n"\
             f"Correo: {correo}\n"\
             f"Edad: {edad}\n"\
             f"Ciudad: {ciudad.upper()}"

    # Se imprime el reporte en pantalla
    print(cadena)


# Definición de la función que genera un correo institucional
def generar_correo(nombre, apellido):
    """
    Función que genera un correo institucional en función del nombre y apellido
    pasados como parámetros.
    Los datos se convierten a minúsculas para mantener un formato estándar.
    """

    # Se convierten los valores de nombre y apellido a minúsculas, con la
    # función lower()
    nombre = nombre.lower()
    apellido = apellido.lower()

    # Se construye la dirección de correo electrónico
    correo = f"{nombre}_{apellido}@utpl.edu.ec"

    # Se retorna el correo generado
    return correo
