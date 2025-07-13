from collections import Counter

def validacionMensaje(mensaje, cofre):
    mensaje = mensaje.replace(" ", "").lower()
    cofre = cofre.replace(" ", "").lower()
    
    letras_mensaje = Counter(mensaje)
    letras_cofre = Counter(cofre)
    
    for letra, cantidad in letras_mensaje.items():
        if letras_cofre[letra] < cantidad:
            return False
    return True


# print(validacionMensaje("hola mundo", "holamundo"))
# print(validacionMensaje("test", "dasiknujfewrnoiuj"))