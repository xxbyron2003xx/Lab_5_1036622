from modelos.persona import Person
import os

def conversation_assign(modelo):
    path = "inputs"
    # Lista todos los archivos en el directorio
    all_files = os.listdir(path)
    # Filtra solo aquellos que comienzan con "REC-" + dpi de la persona
    associated_files = [file for file in all_files if file.startswith(f'CONV-{modelo.dpi}-') and file.endswith('.txt')]
    # Lista que almacenará el contenido de los archivos
    contents = []
    # Lee y añade el contenido de cada archivo a la lista
    for file in associated_files:
        with open(os.path.join(path, file), 'r') as f:
            content = f.read()
            contents.append(content)
    
    return contents