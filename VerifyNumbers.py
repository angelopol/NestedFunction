def VerifyNumbers(var):

    '''
    Función para verificar si un string es númerico o no.

    var = variable a verificar.
    
    errors = lista con los errores, en caso de haberlos. 
    '''

    errors = []

    for i in var:

        # Se recorre la variable dentro de un for.

        if i not in '0123456789':

            # Si el caracter seleccionado no esta dentro del string numerico, se introduce la variable en la lista "errors".

            errors.append(i)
        
    if len(errors) == 0:

        # Si la lista errors esta vacia significa que no hubo ningun error, por lo tanto se retorna True.

        return True, True
    
    else:

        # Si la lista no esta vacia hubieron errores, se retorna False y la lista "errors" con los errores.

        return False, errors