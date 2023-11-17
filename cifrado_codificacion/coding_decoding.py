from companies import companies as contexto

def obtener_numero_codificacion(companies):
    return sum([contexto.index(compania) for compania in companies if compania in contexto])

def codificar(dpi, companies):
    numero_codificacion = obtener_numero_codificacion(companies)
    
    # Codificar el DPI usando XOR con el n�mero de codificaci�n
    dpi_codificado = int(dpi) ^ numero_codificacion
    
    # A�adir el n�mero de codificaci�n al final del DPI codificado para usarlo en la decodificaci�n
    return int(str(dpi_codificado) + str(numero_codificacion).zfill(4))

def decodificar(dpi_codificado_con_info):
    # Extraer el n�mero de codificaci�n del final del DPI
    numero_codificacion = int(str(dpi_codificado_con_info)[-4:])
    
    # Extraer el DPI codificado sin la informaci�n a�adida
    dpi_codificado = int(str(dpi_codificado_con_info)[:-4])
    
    # Decodificar usando XOR
    return dpi_codificado ^ numero_codificacion