from table import table
from center import center

def TableCenter(number):

    '''
    Funcion para centrar el resultado obtenido por la funcion "table".

    number = numero ingresado por el usuario.
    
    result = resultado obtenido por "table".

    TableResult = variable generado por el for, representa cada linea de la tabla dentro de "result".
    '''

    result = table(number)

    for TableResult in result:

        #Se imprime y centran cada linea de la tabla.

        print(center(TableResult))