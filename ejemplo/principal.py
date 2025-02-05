"""
    Importar funciones desde el módulo 'mis_funciones'.
"""

# Se importa las funciones desde el módulo 'mis_funciones'
from mis_funciones import imprimir_reporte, generar_correo
# Alternativamente, se podría importar todo el módulo con: from mis_funciones import *

# Definición de una función que solicita datos al usuario por teclado
def ingresar_datos():
    """
    Función que solicita datos de un usuario por teclado y genera un reporte, 
    llamando a funciones que están en otra módulo
    """

    # Ingreso de datos por teclado
    nombre_ingresado = input("Ingresar nombre: ")
    apellido_ingresado = input("Ingresar apellido: ")

    edad_ingresada = input("Ingresar edad: ")
    edad_ingresada = int(edad_ingresada)  # Conversión a entero

    ciudad_ingresada = input("Ingresar ciudad: ")

    # Se hace uso de la función generar_correo del módulo importado
    # Se genera el correo con base en los datos ingresados
    correo_generado = generar_correo(nombre_ingresado, apellido_ingresado)

    # Se llama a la función imprimir_reporte (proveniente del módulo importado)
    # Se envían los argumentos correspondientes para generar la salida en pantalla
    imprimir_reporte(nombre_ingresado, apellido_ingresado, edad_ingresada,
                     ciudad_ingresada, correo_generado)


if __name__ == "__main__":
    #
    # Se llama a la función ingresar_datos para iniciar la ingreso de información
    ingresar_datos()

