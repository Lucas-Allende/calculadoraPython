"""Hacer una calculadora. Para ello el programa iniciará y contará con un menú de opciones:
1. Ingresar 1er operando (A=x)
2. Ingresar 2do operando (B=y)
3. Calcular todas las operaciones
a) Calcular la suma (A+B)
b) Calcular la resta (A-B)
c) Calcular la división(A/B)
d) Calcular la multiplicación(A*B)
e) Calcular factorial(A!)
4. Informar resultados
a) “El resultado de A+B es: r”
b) “El resultado de A-B es: r”
c) “El resultado de A/B es: r” o “No es posible dividir por cero”
d) “El resultado de A*B es: r”
e) “El factorial de A es: r1 y El factorial de B es: r2”
5. Salir
• Todas las funciones matemáticas del menú se deberán realizar en una biblioteca aparte,que contenga las funciones
para realizar las cinco operaciones.
• En el menú deberán aparecer los valores actuales cargados en los operandos A y B(donde dice “x” e “y” en el ejemplo,
se debe mostrar el número cargado)
• Deberán contemplarse los casos de error (división por cero, etc.)
• Documentar todas las funciones
"""


from funciones_calculadora import *

"""Funcion que muestra un menu de opciones
    """
def menu(primer_numero, segundo_numero)->str:
    limpiarPantalla()
    print(f"{'\n Menu de opciones' :^50s}")
    print(f"1-Ingresar primer operando: A = {primer_operando} ")
    print(f"2-Ingresar segundo operando: B = {segundo_operando} ")
    print("3-Calcular operacion: ")
    print("4-Mostrar resultado: ")
    print("5-Salir ")
    return input("Ingrese opcion: ")

#-------------------------------------------------------

primer_operando = 0
segundo_operando = 0

flag_primer_operando = 0
flag_segundo_operando = 0

while True:
    match menu(primer_operando,segundo_operando):
        case "1":
            primer_operando = pedir_numero()
            flag_primer_operando = 1
        case "2":
            if flag_primer_operando == 0:
                print("Primero debe ingresar el primer operando...")
            else:
                segundo_operando = pedir_numero()
                flag_segundo_operando = 1
        case "3":
            if flag_primer_operando == 0 or flag_segundo_operando == 0:
                print("Primero debe ingresar ambos operandos...")
            else:
                resultado_suma = sumar(primer_operando, segundo_operando)
                resultado_resta = restar(primer_operando, segundo_operando)
                resultado_multiplicar = multiplicar(primer_operando, segundo_operando)

                try:
                    resultado_dividir = dividir(primer_operando, segundo_operando)
                    if resultado_dividir is None:
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    resultado_dividir = "No es posible dividir por cero"

                try:
                    resultado_factorial_n1 = factorial(primer_operando)
                except ValueError as e:
                    resultado_factorial_n1 = str(e)
                
                try:
                    resultado_factorial_n2 = factorial(segundo_operando)
                except ValueError as e:
                    resultado_factorial_n2 = str(e)

                print("Las operaciones fueron calculadas con exito...")
        case "4":
            print(f"El resultado de {primer_operando} + {segundo_operando} es: {resultado_suma}")
            print(f"El resultado de {primer_operando} - {segundo_operando} es: {resultado_resta}")
            print(f"El resultado de {primer_operando} * {segundo_operando} es: {resultado_multiplicar}")
            print(f"El resultado de {primer_operando} / {segundo_operando} es: {resultado_dividir}") 



            print(f"El factorial de A es {resultado_factorial_n1} y el factorial de B es {resultado_factorial_n2}")

        case "5":
            break
    pausar()

print("Fin del programa")

    

