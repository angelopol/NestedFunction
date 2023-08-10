def center(word):

    '''
    Función para centrar un string.

    word = string que debe ser centrado.

    long = cantidad de letras en pantalla. *Modificar con la cantidad de letras que pueden ser mostradas verticalmente en tu pantalla*

    num = calculo de cantidad de espacios hasta llegar al centro de la pantalla.

    word = string final ya centrado. 
    '''

    long = int(177 / 2)

    num = int(long - (int(len(word)) / 2))

    espacio = " "

    word = espacio * num + word

    return word