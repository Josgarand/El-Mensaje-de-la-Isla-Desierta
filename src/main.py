from collections import Counter
# import string
import re

def validacionMensaje(mensaje:str = None, cofre:str = None) -> bool:
    
    mensaje = mensaje.replace(" ", "").lower()
    cofre = cofre.replace(" ", "").lower()
    
    if not re.fullmatch(r'[a-záéíóúüñ]+', mensaje, re.IGNORECASE):
        return False
    if not re.fullmatch(r'[a-záéíóúüñ]+', cofre, re.IGNORECASE):
        return False
    
    letras_mensaje = Counter(mensaje)
    letras_cofre = Counter(cofre)
    
    # TODO: DOCUMENTAR ESTO
    # permitidos = set(string.ascii_lowercase)    
    
    # if not all(m in permitidos for m in mensaje):
    #     # print("\ncaracteres no permitidos en mansaje")
    #     return False
    
    # if not all(c in permitidos for c in cofre):
    #     return False
    for letra, cantidad in letras_mensaje.items():
        if letras_cofre[letra] < cantidad:
            return False
    return True

# print(validacionMensaje("SOS", "PELIGROSOS"))
# print(validacionMensaje("SYS", "PELIGROSOS"))
