#define la funcion llamadqa encontrar_el_mayor que resibe el parametro de lista 
def encontrar_el_mayor(lista):
 #asume que el primer numero de la lista es el mayor   
    mayor = lista[0]
# recorre cada numero de la lista para compararlos y ver cual es el numero mayor para al final devolver el valor guardado en mayor
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
# define la ffuncion prinsipal del programa, se crea una lista con numeros para que al final imprima el resultado 
def main():
    numeros = [2, 5, 8, 13, 9, 1]
    print("El número mayor es:", encontrar_el_mayor(numeros))

main()


