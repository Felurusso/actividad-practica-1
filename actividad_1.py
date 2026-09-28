def recibir_columnas (rol,columnas,lista_roles):
    '''esta funcion, recibe el diccionario de roles y el rol a buscar.
        Una vez se decifra pertenece a la columna del senso, se almacena en un nuevo diccionario,
        el cual se ordena de acuerdo a los parametros delrol ingresado, y se almacena en la lista de roles,
        en su respectiva posicion'''
    
    if (rol in lista_roles):

        nuevo_diccionario =  {clave:valor for clave,valor in columnas.items() if clave in lista_roles[rol][0]}
        print (type(nuevo_diccionario))

        nombres,criterio,orden,mostrar = nuevo_diccionario[:4]

        nuevo_diccionario = dict(sorted(nuevo_diccionario.items(), key=criterios.get(criterio),
                                         reverse = orden.get(orden)))
        
        print('nuevo diccionario: ',nuevo_diccionario)

       #'''MÉTODO DESCARTADO - POCO EFICIENTE
       # #if lista_roles [rol][1] == 'alfabeticamente' and lista_roles [rol][2] == 'A':
       #    nuevo_diccionario = dict(sorted (nuevo_diccionario.items(),key=lambda item: item[0]))
       #elif lista_roles [rol][1] == 'alfabeticamente' and lista_roles [rol][2] == 'B':
       #    nuevo_diccionario = dict(sorted (nuevo_diccionario.items(),key=lambda item: item[0], reverse = True))

       #elif lista_roles [rol][1] == 'porcentaje' and lista_roles [rol][2] == 'A':
       #    nuevo_diccionario = dict(sorted (nuevo_diccionario.items(), key=lambda item: item[1][1]))
       #elif lista_roles [rol][1] == 'porcentaje' and lista_roles [rol][2] == 'B':
       #    nuevo_diccionario = dict(sorted (nuevo_diccionario.items(), key=lambda item: item[1][1], reverse = True))

        lista_roles[rol].append(nuevo_diccionario)
        
        if lista_roles[rol][3] is not None:
            porcentaje = lista_roles[rol] [3]
            print('mostrando las columnas con un porcentaje mayor o igual a ',lista_roles[rol] [3],' ... ')
            print (dict(filter(lambda item: item [1][1] >= porcentaje ,nuevo_diccionario.items())))
    
    else:
        print ('el rol de ', rol ,' no se encuentra en la lista')
    
    #fin de la funcion o.O

def informar_no_especificados (columnas):
    '''esta funcion recibe la lista de roles y si, el rol que se ingresó
       no se encuentra en la lista, se imprimen todas las columnas
       ordenadas por completitud, de forma descendente.'''
    
    print ('el rol ingresado no se encuentra en la lista, mostrando' \
    ' todas las columnas ordenadas por completitud de forma descendente')
    print (sorted (columnas.items(), key=lambda item: item[1][1], reverse = True))
    #print (nuevo_diccionario)

    #fin de la funcion

criterios = {'alfabeticamente' : lambda item: item[0],
             'porcentaje': lambda item: item [1][1]}

orden = {'A': False, 'B': True}


#programa principal
#-------------------
columnas = {'estado':[range(1,4),0.54], 'año':[int,1.00],
            'cat_ocup':[int,0.15],    'edad':[int,0.45],  'region':[str,0.32],
            'aglomerado': [int,0.78], 'mas_500':[str,0.30], 'trimestre':[range(1,5), 0.80],
            'itf': [int,0.87],'gfeccfr':[int,0.10]}

lista_roles = {'docente':[['año','estado','region','aglomerado'],'alfabeticamente','A',None],
         'investigador':[['año','estado','cat_ocup','gfeccfr'],'porcentaje','B',0.35],
         'analista':[['año','edad','cat_ocup','trimestre'],'alfabeticamente','B',0.8]}

rol_input = input('ingrese rol a buscar: ')
recibir_columnas (rol_input,columnas,lista_roles)

if rol_input in lista_roles:
    print(lista_roles[rol_input])

else:
    informar_no_especificados (columnas)


