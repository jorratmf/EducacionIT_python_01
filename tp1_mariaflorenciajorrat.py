'''
PARTE 1
1. Crea un variable llamada conejos y asígnale el valor 126. 
2. Crea una variable llamada zanahorias y asígnale el valor 0. 
3. Muestra el contenido de la variable conejos. 
4. Modifica el valor de la variable conejos por 150. 
5. Copia el valor de la variable conejos en la variable zanahorias. 
6. Imprime el valor de las dos variables con print(). 
7. Modifica el valor de conejos por 250 y vuelve a mostrar las dos 
variables. 
'''
print('PARTE 1')
conejos = 126
zanahorias = 0
print(conejos)
conejos = 150
zanahorias = conejos
print(conejos, zanahorias)
conejos = 250
print(conejos, zanahorias)
print('\n')


'''
PARTE 2
1. Calcula las siguientes operaciones y muéstralas en pantalla: 
• 3 mas 6
• 5 menos 4
• 6 multiplicado por 8
• 8 dividido 2
• Division entera de 6 dividido 2
• 3 multiplicado por 5
2. Coloca los paréntesis en su lugar correspondiente para la expresión 
4 + 5 * 6 de forma que: 
a. Python realice primero las sumas. 
b. Python realice primero las multiplicaciones.
'''
print('PARTE 2')
print(3 + 6)
print(5 - 4)
print(6 * 8)
print(8 / 2)
print(6 // 2)
print(3 * 5)
print((4 + 5) * 6)
print(4 + (5 * 6))
print('\n')


'''
PARTE 3
1. Escribe la palabra elefante dentro de una variable llamada animal. 
2. Escribe la palabra rosa dentro de una variable llamada color. 
3. Crea una variable llamada imagina donde se almacenen las dos variables 
anteriores: animal y color dando como resultado un dato de tipo string igual a 
“elefante rosa”. 
4. PUNTO EXTRA: convertir el contenido de la variable imagina a MAYÚSCULAS, 
utilizando un metodo de strings.
'''
print('PARTE 3')
animal = "elefante"
color = "rosa"
imagina = animal + " " + color
print(imagina)
imagina = imagina.upper()
print(imagina)