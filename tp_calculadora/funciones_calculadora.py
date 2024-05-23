
"""Funcion para limpiar pantalla 
    """
def limpiarPantalla():
    import os
    os.system("cls")

    """Funcion que pausa el programa hasta que el usuario presione una tecla
    """
def pausar():
    import os
    os.system("pause")


def pedir_numero():
    """Pide y valida un entero

    Returns:
        _type_: Retorna el numero ingresado por el usuario
    """
    while True:
        try:
            num = int(input("Ingrese un número: "))
            return num
        except ValueError:
            print("Por favor, ingrese un número válido.")



def sumar(num_uno:int, num_dos:int)->int:
    """Suma dos numeros enteros

    Args:
        num_uno (int): primer operando
        num_dos (int): segundo operando

    Returns:
        int: retorna el resultado de la suma
    """
    resultado_suma = num_uno + num_dos
    
    return resultado_suma


def restar(num_uno:int, num_dos:int)->int:
    """Funcion que realiza una resta

    Args:
        num_uno (int): primer operando ingresado
        num_dos (int): segundo operando ingresado

    Returns:
        int: retorna el resultado de la resta de primer operando - segundo operando
    """
    resultado_resta = num_uno - num_dos
    
    return resultado_resta

def multiplicar(num_uno:int, num_dos:int)->int:
    """Funcion que multiplica dos operandos

    Args:
        num_uno (int): primer operando ingresado
        num_dos (int): segundo operando ingresado

    Returns:
        int: retorna el resultado de la multiplicacion de ambos operandos
    """
    resultado_multiplicar = num_uno * num_dos
    
    return resultado_multiplicar

def dividir(num_uno:int, num_dos:int)->float:
    """funcion que divide primer operando / segundo operando

    Args:
        num_uno (int): primer operando ingresado
        num_dos (int): segundo operando ingresado

    Returns:
        float: retorna el resultado de la division
    """
    if num_dos == 0:
        #print("No se puede dividir por cero ")
        return None
    else:
        resultado_division = num_uno / num_dos 
        return resultado_division
    
def factorial(n:int)->int:
    """Funcion que calcula el factorial de un numero

    Args:
        n (int): Operando ingresado

    Raises:
        ValueError: Error en caso de que se ingresen numeros negativos

    Returns:
        int: retorna el resultado del factorial del numero ingresado
    """
    if n < 0:
        raise ValueError("El factorial es solo para numeros naturales")
    
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact
