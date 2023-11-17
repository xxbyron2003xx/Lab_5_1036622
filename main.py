from modelos.persona import Person
from arbol import ArbolBinario
from personAssings.conversations_assign import conversation_assign
from personAssings.letters_assign import letters_assign
from compresiones.RLE import comprimir_rle, descomprimir_rle
from cifrado_codificacion.cifrado_descrifrado import encrypt, decrypt
from cifrado_codificacion.coding_decoding import codificar, decodificar
from RSA.RSA import RSA
from recluiters import recluiters
import json
import csv


jsonArbol = ArbolBinario()

def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)

    return prime_list

from datetime import datetime
ahora = datetime.now()
dia = ahora.day

primo = primesInRange(0,75)
if(dia == primo[10]):
    dia+=1
    
rsa = RSA(primo[10], primo[dia])

menu = ""

while(menu != None):
    print("1. Cargar archivo\n")
    print("2. Buscar por nombre (rango)\n")
    print("3. Buscar por dpi (individual)\n")
    print("4. Eliminar por Nombre (rango)\n")
    print("5. Eliminar por dpi (individual)\n")
    print("6. Actualizar por Nombre (rango)\n")
    print("7. Actualizar por dpi (individual)\n")
    print("8. Codificar por dpi\n")
    print("9. Decodificar por dpi\n")
    print("10. Comprimir Cartas (individual)\n")
    print("11. Descomprimir Cartas (individual)\n")
    print("12. Cifrar conversaciones (individual)\n")
    print("13. Descifrar conversaciones (individual)\n")
    print("14. Generar llave privada\n")
    print("15. Obtener informacion\n")
    print("16. Salir")
    menu = input()

    if(menu == "1"):
        print("Cargando archivo...")
        
        with open ('input.csv') as archivoPersonas:
            lector = csv.reader(archivoPersonas, delimiter =";")
            
            for fila in lector:
                jsonPersona = Person.from_json(str(fila[1]))
                jsonPersona.letter = letters_assign(jsonPersona)
                jsonPersona.conversation = conversation_assign(jsonPersona)
                
                if fila[0] == "INSERT":
                    jsonArbol.insertar(jsonPersona)
                    
                elif fila[0] == "PATCH":
                    if ((jsonArbol.buscar(jsonPersona))!= None):
                        jsonPersonaPatch = jsonArbol.buscar(jsonPersona)
                        jsonPersonaPatch.datebirth = jsonPersona.datebirth
                        jsonPersonaPatch.address = jsonPersona.address
                        jsonPersonaPatch.companies = jsonPersona.companies
                        jsonPersonaPatch.letter = jsonPersona.letter
                        jsonPersonaPatch.conversation = jsonPersona.conversation   
                        jsonPersonaPatch.recluiter = jsonPersona.recluiter
                        jsonArbol.eliminar(jsonPersona)
                        jsonArbol.insertar(jsonPersonaPatch)
                        
                    else:
                        print("No se encontro a la persona a la cual quiere ser actualizada.")
                        
                elif fila[0] == "DELETE":
                     jsonArbol.eliminar(jsonPersona)
                     
                else:
                    print("No se encontro ninguna de las opciones.")
                    
        print("Se cargo correctamente!")
        
    elif(menu == "2"):
        print("Buscar por nombre")
        print("Coloque el nombre de las personas que quiere buscar:")
        nombre = input()
        lista_persona_nombre = jsonArbol.buscar_por_nombre(nombre.lower())
        i =0
        while i < len(lista_persona_nombre):
            print("Nombre:" + lista_persona_nombre[i].name)
            print("Dpi:" + lista_persona_nombre[i].dpi)
            print("Fecha de nacimiento:" + lista_persona_nombre[i].datebirth)
            print("Direccion:" + lista_persona_nombre[i].address)
            print("Companias:" + str(lista_persona_nombre[i].companies))
            print("No. de Companias:" + str(len(lista_persona_nombre[i].companies)))
            print("Cartas:" + str(lista_persona_nombre[i].letter))
            print("No. de Cartas:" + str(len(lista_persona_nombre[i].letter)))
            print("Conversaciones:" + str(lista_persona_nombre[i].conversation))
            print("No. de Conversaciones:" + str(len(lista_persona_nombre[i].conversation)))
            print("Reclutador:" + str(lista_persona_nombre[i].recluiter))
            print('\n')
            i += 1
        print("Se encontraron:" + str(i) +" resultados.")
        
    elif(menu == "3"):
        print("Buscar por dpi")
        print("Coloque el dpi de la persona que quiere buscar:")
        dpi = input()
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
            
        else:
            print("Nombre:" + persona_dpi.name)
            print("Dpi:" + persona_dpi.dpi)
            print("Fecha de nacimiento:" + persona_dpi.datebirth)
            print("Direccion:" + persona_dpi.address)
            print('\n')
            print("Companias:" + str(persona_dpi.companies))
            print('\n')
            print("No. de Companias:" + str(len(persona_dpi.companies)))
            print('\n')
            print("Cartas:" + str(persona_dpi.letter))
            print('\n')
            print("No. de Cartas:" + str(len(persona_dpi.letter)))
            print('\n')
            print("Conversaciones:" + str(persona_dpi.conversation))
            print('\n')
            print("No. de Conversaciones:" + str(len(persona_dpi.conversation)))
            print('\n')
            print("Reclutador:" + str(persona_dpi.recluiter))
            print('\n')

    elif(menu == "4"):
        print("Eliminar por Nombre")
        print("Coloque el nombre de las personas que quiere eliminar:")
        nombre = input()
        lista_persona_nombre = jsonArbol.buscar_por_nombre(nombre.lower())
        i =0
        while i < len(lista_persona_nombre):
            jsonArbol.eliminar(lista_persona_nombre[i])
            i += 1
        print("Se eliminaron: " + str(i) +" personas.")

    elif(menu == "5"):
        print("Eliminar por dpi")
        print("Coloque el dpi de la personas que quiere eliminar:")
        nombre = input()
        persona_dpi = jsonArbol.buscar_por_dpi(nombre)
        if(persona_dpi == None):
            print("No se encontro a la persona")
            
        else:
            jsonArbol.eliminar(persona_dpi)
            print("Se elimino correctamene!")
        
    elif(menu == "6"):
        print("Actualizar por nombre")
        print("Coloque el nombre de las personas que quiere actualizar:")
        nombre = input()
        lista_persona_nombre = jsonArbol.buscar_por_nombre(nombre.lower())
        print("Coloque la Fecha de nacimiento (en caso de no querer cambiar dar ENTER):")
        fecha = input()
        print("Coloque la direccion (en caso de no querer cambiar dar ENTER):")
        direccion = input()
        if (fecha != '') & (direccion == ''):
            i =0
            while i < len(lista_persona_nombre):
                lista_persona_nombre[i].datebirth = fecha
                i += 1
                
        elif (fecha == '') & (direccion != ''):
            i =0
            while i < len(lista_persona_nombre):
                lista_persona_nombre[i].address = direccion
                i += 1
                
        elif (fecha != '') & (direccion != ''):
            i =0
            while i < len(lista_persona_nombre):
                lista_persona_nombre[i].datebirth = fecha
                lista_persona_nombre[i].address = direccion
                i += 1
                
        else:
            print("No se hacen cambios")

    elif(menu == "7"):
        print("Actualizar por dpi")
        print("Coloque el dpi de la persona que quiere actualizar:")
        dpi = input()
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
            
        else:
            print("Coloque la Fecha de nacimiento (en caso de no querer cambiar dar ENTER):")
            fecha = input()
            print("Coloque la direccion (en caso de no querer cambiar dar ENTER):")
            direccion = input()
            if (fecha != '') & (direccion == ''):
                persona_dpi.datebirth = fecha
            
            elif (fecha == '') & (direccion != ''):
                persona_dpi.address = direccion
            
            elif (fecha != '') & (direccion != ''):
                persona_dpi.datebirth = fecha
                persona_dpi.address = direccion
            
            else:
                print("No se hacen cambios")

    elif(menu == "8"):
        print("Codificando el atributo \"dpi\" de los objetos \"persona\"...")
        dpi = input("Ingrese el dpi el cual quiere codificar... \n")
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
            
        else:
            persona_dpi_codificado = codificar(dpi, persona_dpi.companies)
            print(f"Codificacion exitosa! , el numero de dpi codificado es: {persona_dpi_codificado}")
        
    elif(menu == "9"):
        print("Decodificacion por dpi encodeing")
        dpiencodeing = input("Ingrese el dpi codificado de la persona que quiere decodificar \n")
        dpi = str(decodificar(dpiencodeing))
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
            
        else:
            print("Nombre:" + persona_dpi.name)
            print("Dpi:" + persona_dpi.dpi)
            print("Fecha de nacimiento:" + persona_dpi.datebirth)
            print("Direccion:" + persona_dpi.address)
            print("Companias:" + str(persona_dpi.companies))
            print('\n')
            print("Cartas:" + str(persona_dpi.letter))
            print('\n')
            print("No. de Cartas:" + str(len(persona_dpi.letter)))
            print('\n')
            print("Conversaciones:" + str(persona_dpi.conversation))
            print('\n')
            print("No. de Conversaciones:" + str(len(persona_dpi.conversation)))
            print('\n')
            
    elif(menu == "10"):
        dpi = input("Ingrese el dpi del cual quiere comprimir las cartas \n")
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
        else:
            i = 0
            while i < len(persona_dpi.letter):
                persona_dpi.letter[i] = comprimir_rle(persona_dpi.letter[i])
                i += 1
            print("Se han comprimido las cartas!")
        
    elif(menu == "11"):
        dpi = input("Ingrese el dpi del cual quiere descomprimir las cartas \n")
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
        else:
            i = 0
            while i < len(persona_dpi.letter):
                persona_dpi.letter[i] = descomprimir_rle(persona_dpi.letter[i])
                i += 1
            print("Se han descomprimido las cartas!")
            
    elif(menu == "12"):
        dpi = input("Ingrese el dpi del cual quiere cifrar las conversaciones \n")
        password = input("Ingrese la contrasena de cifrado \n")
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
        else:
            i = 0
            while i < len(persona_dpi.conversation):
                persona_dpi.conversation[i] = encrypt(persona_dpi.conversation[i], password)
                i += 1
            print("Se han cifrado las conversaciones! \n")

    elif(menu == "13"):
        dpi = input("Ingrese el dpi del cual quiere descifrar las conversaciones \n")
        password = input("Ingrese la contrasena de descifrado \n")
        persona_dpi = jsonArbol.buscar_por_dpi(dpi)
        if(persona_dpi == None):
            print("No se encontro a la persona")
        else:
            i = 0
            while i < len(persona_dpi.conversation):
                if(decrypt(persona_dpi.conversation[i], password) != None):
                    persona_dpi.conversation[i] = decrypt(persona_dpi.conversation[i], password)
                    print("Se han descifrado la conversacion: " + str(i+1))
                i += 1
    
    elif(menu == "14"):
        reclutador = input("Ingrese su nombre de usuario:\n")
        if(not(reclutador in recluiters)):
            print("No eres reclutador de Talent Hub")
            continue
        
        dpiPersona = input("Ingrese el dpi de la persona a generar llave:\n")
        if(jsonArbol.buscar_por_dpi(dpiPersona) == None):
            print("No existe la persona buscada")
            continue
        
        persona = jsonArbol.buscar_por_dpi(dpiPersona)
        if(persona.recluiter != reclutador):
            print("No eres el reclutador de esta persona")
            continue
        
        crypt_rsa = rsa.crypt(str(reclutador+dpiPersona))
        print("Tu clave privada es: " + str(crypt_rsa))
        
    elif(menu == "15"):
        reclutador = input("Ingrese su nombre de usuario:\n")
        if(not(reclutador in recluiters)):
            print("No eres reclutador de Talent Hub")
            continue
        
        dpiPersona = input("Ingrese el dpi de la persona a generar llave:\n")
        if(jsonArbol.buscar_por_dpi(dpiPersona) == None):
            print("No existe la persona buscada")
            continue
        
        persona = jsonArbol.buscar_por_dpi(dpiPersona)
        if(persona.recluiter != reclutador):
            print("No eres el reclutador de esta persona")
            continue
        
        llavePrivada = input("Ingrese su llave privada:\n")
        comprobacion = rsa.crypt(str(reclutador+dpiPersona))
        if(llavePrivada != str(comprobacion)):
            print("Llave incorrecta, no puedes acceder a la informacion.")
            continue
        
        print("Informacion del usuario:")
        print('\n')
        print("Nombre:" + persona.name)
        print("Dpi:" + persona.dpi)
        print("Direccion:" + persona.address)
        print('\n')
        print("Companias:" + str(persona.companies))
        print('\n')
        print("No. de Companias:" + str(len(persona.companies)))
        print('\n')
        print("Cartas:" + str(persona.letter))
        print('\n')
        print("No. de Cartas:" + str(len(persona.letter)))
        print('\n')
        print("Conversaciones:" + str(persona.conversation))
        print('\n')
        print("No. de Conversaciones:" + str(len(persona.conversation)))
        print('\n')
        print("Reclutador:" + str(persona.recluiter))
        print('\n')

    elif(menu == "16"):
        menu = None
