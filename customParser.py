def Convert(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    return res_dct 

def parser(nombreArch,nombreDTD):
    xmlValid = False
    xmlMesg= ''
    dtdValid = False
    dtdMesg= ''

    list = []
    copia_list = []
    min = 0
    max = 0
    indice = 0
    list_apertura = []
    list_cierre = []
    completo = ''

    # Abrir archivo XML
    # nombreArch = input("Nombre del XML: ")
    arch = open(nombreArch, 'r')

    # Eliminar el enter de cada linea
    for linea in arch:
        list.append(linea.replace("\n", ''))

    # Agregar espacio al final de la lista
    list.append(" ")

    # Copiar los elementos a una lista auxiliar
    for ele in list:
        copia_list.append(ele)

    # Revisamos cuantos <> hay
    for cosa in list[2:]:
        for caracter in cosa:
            if caracter == '<':
                min += 1
            elif caracter == '>':
                max += 1

    chequeo = True
    if min % 2 == 0 and max % 2 == 0:
        print("El numero de Tags es correcto")
    else:
        min = 0
        max = 0
        for line in list[2:]:
            if min != max:
                print("Error: " + str(indice + 2))
                chequeo = False
                break
            indice += 1
            for letra in line:
                if letra == '<':
                    min += 1
                elif letra == '>':
                    max += 1

    # Guardamos los nombres de los tags del XML
    lista_aux = []
    for elem in copia_list:
        completo += elem
        for caracelem in elem:
            if caracelem == '<':
                lista_aux.append(completo.split("<"))

    lista_aux2 = []
    aux = ''
    for etiqueta in lista_aux[-1]:
        aux += etiqueta
        for car in etiqueta:
            if car == '>':
                lista_aux2.append(aux.split('>'))

    # Hacemos una pila para comparar cada tag
    pila_abierto = []
    pila_cerrado = []
    lista_intermedia = []
    lista_nueva = []
    lista_aux = []
    letrero = ''
    cerrado = ''
    for l in lista_aux2[-1]:
        for l2 in l:
            for carac in l2:
                letrero += carac
        pila_abierto.append(letrero)
        letrero = ''

    for elemen in pila_abierto[2:]:
        for caracel in elemen:
            if caracel == '/':
                lista_intermedia.append(elemen)
                pila_abierto.remove(elemen)

    for el in lista_intermedia:
        cerrado += el
        for carc in el:
            if carc == '/':
                lista_nueva.append(cerrado.split("/"))
                cerrado = ''

    for i in lista_nueva:
        for elemento in i[1:]:
            pila_cerrado.append(elemento)

    for objeto in pila_abierto[1:]:
        lista_aux.append(objeto)

    # Quitamos el espacio del final de la lista
    for blanco in lista_aux:
        if blanco == '':
            lista_aux.remove(blanco)

    # Revisamos que el primer elemento de la lista sea igual al último elemento de la lista de los tags de cierre.
    boleano = False

    if lista_aux[1] == pila_cerrado[-1]:
        boleano = True

    # Revisamos que haya pasado satisfactoriamente por el primer conteo de tags, y si lo hizo, entonces revisamos
    # si el número de tags es igual al número de verdaderos que se tienen.
    if chequeo:
        if len(lista_aux) - 1 != len(pila_cerrado):
            xmlMesg = "Error los tag no estan correctos"
        else:
            xmlMesg = "XML Formado correctamente."
            xmlValid = True

    # Abrimos archivo DTD.
    # nombreDTD = input("Escriba el DTD: ")
    dtd = open(nombreDTD , 'r')

    listadtd = []

    # Guardamos los nombres de los tags del DTD
    for lin in dtd:
        listadtd.append(lin.split(' ')[1])

    # Comparamos al igual que anteriormente que si el tamaño de la lista de tags del dtd es igual a la cantidad de verdaderos,
    # ya que si lo es, esto significa que el XML se encuentra pareado con el DTD.
    dtd_dict = {}
    for i in lista_aux:
        if (i == lista_aux[0]):
            continue
        dtd_dict[i] = i

    if len(listadtd) ==  len(dtd_dict):
        dtdMesg = "El XML corresponde con el DTD"
        dtdValid = True
    else:
        dtdMesg = "El XML no corresponde con el DTD"

    return xmlMesg,xmlValid,dtdMesg,dtdValid
