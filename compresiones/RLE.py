#Run-Length Encoding (RLE)
def comprimir_rle(texto):
    if not texto:
        return ""
    
    comprimido = []
    cuenta_actual = 1
    caracter_anterior = texto[0]
    
    for caracter in texto[1:]:
        if caracter == caracter_anterior:
            cuenta_actual += 1
        else:
            comprimido.append(str(cuenta_actual) + caracter_anterior)
            cuenta_actual = 1
            caracter_anterior = caracter
            
    comprimido.append(str(cuenta_actual) + caracter_anterior)
    
    return ''.join(comprimido)

def descomprimir_rle(texto_comprimido):
    if not texto_comprimido:
        return ""
    
    descomprimido = []
    numero = ""
    
    for caracter in texto_comprimido:
        if caracter.isdigit():
            numero += caracter
        else:
            descomprimido.append(int(numero) * caracter)
            numero = ""
    
    return ''.join(descomprimido)