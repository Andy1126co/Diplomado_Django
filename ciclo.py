mi_lista = ['Daniel','Andres','Lilith']
for i in mi_lista:
    print('hola '+ i +' que tengas buen dia')
    print()

for i in range(len(mi_lista)):
    print(i)

print()
diccionario = {'agua':100000,'gas':40000,'electricidad':60000,'internet':100000}
for llave, valor in diccionario.items():
    print(llave,valor)
