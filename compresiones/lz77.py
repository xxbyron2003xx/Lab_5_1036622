def comprimir_lz77(texto, max_longitud_ventana=255):
    i = 0
    longitud = len(texto)
    diccionario = ""
    resultado = []

    while i < longitud:
        # Buscar la secuencia más larga que coincida
        match_length = 0
        match_position = 0
        for j in range(max(0, i - max_longitud_ventana), i):
            k = 0
            while k + i < longitud and texto[j + k] == texto[i + k]:
                k += 1
            if k > match_length:
                match_length = k
                match_position = i - j

        # Guardar el resultado
        if match_length >= 2:
            resultado.append((match_position, match_length, texto[i + match_length]))
            i += match_length + 1
        else:
            resultado.append((0, 0, texto[i]))
            i += 1

    return resultado


def descomprimir_lz77(comprimido):
    resultado = []
    for item in comprimido:
        if item[0] == 0 and item[1] == 0:
            resultado.append(item[2])
        else:
            for j in range(0, item[1]):
                resultado.append(resultado[-item[0]])
            resultado.append(item[2])

    return ''.join(resultado)