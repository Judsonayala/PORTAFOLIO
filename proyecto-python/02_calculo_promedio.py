#variable de inicializacion

sum_nota = 0.0
contador_notas = 0
#entrada inicial
print("----------CALCULADORA DE NOTAS----------")
nota_str = input("ingrese una nota (0 para terminar:) ")

#logica de validacion (aseguramos que la primera entrada sea un numero)

try:
    nota_actual = float(nota_str)
except ValueError:
    print("ERROR: ingrese un nuemero valido, cerrando programa")
    exit()

#logica repetitiva (bucle while)
#mientras nota_actual sea diferente de 0 hacer
while nota_actual != 0:
    #proceso de acomular
    sum_nota += nota_actual 
    contador_notas += 1
#control pedir la segunda nota
    nota_str = input("ingrese la siguiente nota (0 para terminar)")

    try:
        nota_actual = float(nota_str)
    except:
       print("ERROR: ingrese nota valida")
       nota_actual = 0 #forzamos la salida del bucle

#calculo final
#si contador_notas es mayor que 0 entonces
if contador_notas > 0:
    promedio = sum_nota / contador_notas
    print("-----RESULTADOS-----")
    print(f"el total de notas acomulada es de {contador_notas} ")
    print(f"el promedio de notas  es: {promedio:.2f}")#punto 2 f es para agregar 2 decimales al promedio
else:
    print("no se ingreso ninguna nota para el calculo")