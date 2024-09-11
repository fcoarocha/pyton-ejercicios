"""
#2
¿ES UN ANAGRAMA?
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

"""

## Lo que entiendo es que hace un tupla de dos valores or linea y se utiliza como diccionario para replace 
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    #print(replacements)
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())  ## Entiendo que remplaza las minusculas y las mayusculas 
    return s

## Introduce las palabras a comparar 
palabra_1 =normalize("Cardiografía")  # Ramo – Armo / Delira – Lidera / Ballena - llenaba / Cardiografía – Radiográfica / Desamparador – Desparramado
palabra_2 =normalize("Radiográfica")  # Agonista – Santiago / Calor – Colar / Reconquistados – Conquistadores / Pronosticación – Contraposición


cadena_1 = list(palabra_1.upper())
cadena_2 = list(palabra_2.upper())

#print(cadena_1)

if cadena_1 == cadena_2:
    print(f"""    ------------------------------------------------------------
    Las palabras "{palabra_1}" y "{palabra_2}" son identicas
    por lo tanto no son anagrama.
    """)
elif cadena_1 != cadena_2:
    print(f"""    ------------------------------------------------------------
    Las palabras "{palabra_1}" y "{palabra_2}" son diferentes!  
    """)
    cadena_1.sort()
    cadena_2.sort()

    if cadena_1==cadena_2:
        print(f"""
        ----------------
        y es un anagrama
        ----------------  
        """)
    elif cadena_1 != cadena_2:
        print(f"""
        -------------------
        y NO es un anagrama  
        -------------------
        """)

print("""
    ---------------------
    Fin del ejercicio 002
    ---------------------
    """)




