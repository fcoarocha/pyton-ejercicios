""" 
#1 EL FAMOSO "FIZZ BUZZ"
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

"""
numeros = 1

def multiplo_de_tres(numero):
    return numero % 3

def multiplo_de_cuatro(numero):
    return numero % 5

while numeros <= 100:
    if multiplo_de_tres(numeros) == 0 and multiplo_de_cuatro(numeros) == 0:
        print("fizzbuzz")
    elif multiplo_de_tres(numeros) == 0:
        print("fizz")   
    elif multiplo_de_cuatro(numeros) == 0:
        print("buzz")
    else:
        print(numeros) 
           
    numeros += 1





