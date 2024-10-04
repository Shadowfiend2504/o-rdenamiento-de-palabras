#Conteo de vocales / invertir frase / imprimir letra por letra hacia abajo
 
texto = "Hola mundo"
vocales="aeiouAEIOU"
conteo_vocales = 0

print(texto)
for caracter in texto:
   print(caracter)
   if caracter in vocales:
        conteo_vocales += 1

print(texto[::-1])
print(conteo_vocales)

#conteo de vocales ingresando palabra por teclado
vocales = "aeiou"
def contar_vocales(texto_o):
    total = 0
    for letra in texto_o:
        if letra in vocales:
            print("Vocal")
            total += 1
            print(total)
    return(total)
texto = input("Escriba un texto: ")
print(f"El tota de minúsculas es: {contar_vocales(texto)}")


#voltear palabra
texto = "Hola mundo"
palabra_volteada = ""
resultado = ""

for caracter in texto:
        palabra_volteada = caracter + palabra_volteada

resultado += palabra_volteada
print(resultado)

#poner en mayuscula la primera letra de cada palabra
texto = "hola mundo"
resultado = ""
nueva_palabra = True

for caracter in texto:
    if nueva_palabra and caracter.isalpha():
        resultado += caracter.upper()
        nueva_palabra = False
    else:
        resultado += caracter
    if caracter == " ":
        nueva_palabra = True

print(resultado)
