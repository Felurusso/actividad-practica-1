import funciones


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
funciones.recibir_columnas (rol_input,columnas,lista_roles)

if rol_input in lista_roles:
    print(lista_roles[rol_input])

else:
    funciones.informar_no_especificados (columnas)


