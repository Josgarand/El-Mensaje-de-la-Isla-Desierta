from collections import Counter
import re

def validacionMensaje(mensaje:str = None, cofre:str = None) -> bool:
    
    mensaje = mensaje.replace(" ", "").lower()
    cofre = cofre.replace(" ", "").lower()
    
    if not re.fullmatch(r'[a-záéíóúüñ0-9]+', mensaje, re.IGNORECASE):
        return False
    if not re.fullmatch(r'[a-záéíóúüñ0-9]+', cofre, re.IGNORECASE):
        return False
    
    letras_mensaje = Counter(mensaje)
    letras_cofre = Counter(cofre)
    
    for letra, cantidad in letras_mensaje.items():
        if letras_cofre[letra] < cantidad:
            return False
    return True

# print(validacionMensaje("SOS", "PELIGROSOS"))
# print(validacionMensaje("SYS", "PELIGROSOS"))