import zlib

def comprimir(texto):
    # Convertir la cadena de texto a bytes
    texto_en_bytes = texto.encode('utf-8')
    # Comprimir los bytes
    comprimido = zlib.compress(texto_en_bytes)
    return comprimido

def descomprimir(datos_comprimidos):
    # Descomprimir los bytes
    texto_en_bytes = zlib.decompress(datos_comprimidos)
    # Convertir los bytes descomprimidos a una cadena de texto
    texto = texto_en_bytes.decode('utf-8')
    return texto