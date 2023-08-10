from VerifyNumbers import VerifyNumbers

def table(num):

    def AddZeros(var, zeros):

        """
        Funcion para añadir ceros a los valores imprimidos en la tabla.

        var = variable a la que se le añaden ceros

        zeros = variable en la que se almacena la cantidad de ceros del ultimo resultado generado por la tabla. 
        """

        if len(var) < zeros:
                
                # Se compara la cantidad de caracteres del numero obtenido con el numero de ceros.

                for j in range(zeros - len(var)):

                    # Se añaden los ceros faltantes al numero obtenido.
                    
                    var = "0" + var

        return var

    '''
    Funcion para imprimir una tabla de multiplicacion del 1 al 10 de forma vertical y centrada. Los ceros generados por la tabla son
    proporcionales a la cantidad de digitos que se obtenga en el ultimo resultado de la tabla, es decir, si el ultimo resultado es 100,
    los numeros de 1 digito, por ejemplo "2", tendran dos ceros por delante para igualar la cantidad de digitos del ultimo resultado,
    por ejmplo "002", los numeros de 2 digitos, por ejemplo "10", tendran solo un cero por delante. Se añadiran tantos ceros como digitos 
    tenga el ultimo resultado.

    num = numero enviado por el usuario.

    tuple = resultado de la funcion "VerifyNumbers".

    numero = copia de la variable "num", que representa el numero que es multiplicado en la tabla.

    ceros = cantidad de ceros del ultimo resultado generado por la tabla.

    i = variable iterable generada por el for, representa el numero que multiplica a "numero" para generar el resultado.

    result = resultado de la multiplicacion entre "i" y "num".

    error = variable generada por el for, representa el error obtenido de la funcion "VerifyNumbers".
    '''

    tabla = []

    # Se verifica si el string ingresado es un numero, y se almacena el resultado en la variable "tuple".
    tuple = VerifyNumbers(num)

    if tuple[0]:

        # Se comprueba si el valor de "tuple" en la posicion 0 es True or False.

        numero = num

        # Se calcula la cantidad de ceros del ultimo resultado.

        ceros = len(str(int(num) * 10))

        # Se añaden los ceros con la funcion "AddZeros"
        numero = AddZeros(numero, ceros)

        num = int(num)
        
        for i in range(10):

            # Se genera la tabla con un for con una cantidad maxima de iteraciones de 10, puesto que solo 10 son necesarias.

            i = i + 1

            # Se calcula el resultado de la multiplicacion entre el numero obtenido y la variable iterable generada por el for.
            
            result = str(num * i)

            # Se añaden los ceros con la funcion "AddZeros"
            result = AddZeros(result, ceros)

            # Se añaden los ceros con la funcion "AddZeros"
            i = AddZeros(str(i), ceros)

            # Se imprimen los datos con forma de tabla mientras son centrados por la funcion "center".

            tabla.append(numero + "x" + str(i) + "=" + result)

    else:

        for error in tuple[1]:

            # Se imprimen los errores obtenidos.

            tabla.append(('"{}" is not a number').format(error))

    return tabla