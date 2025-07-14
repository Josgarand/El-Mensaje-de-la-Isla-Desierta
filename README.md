## El Mensaje de la Isla Desierta

En este proyecto se busca mediante una función poder comprobar si el texto de un mensaje se puede formar con los caracteres que estén disponibles en un cofre. Se ignoran los espacios, se tienen en cuenta los caracteres especiales que no pueden ser introducidos y se permite el uso de acentos.

## Requisitos

Este proyecto está desarrollado en **Python 3.13.1**, pero debería funcionar en versiones anteriores, ya que no utiliza ninguna funcionalidad fuera de la biblioteca estándar.

No es necesario instalar dependencias externas.


## Ejemplos de uso

En el propio código de **main.py** se puede encontrar, comentados en la parte inferior, dos ejemplos para ejecutar la función por si se necesita hacer pruebas de una forma rápida, la forma en la que se llama a la función si se ejecuta desde el mismo archivo será desde un **print()** para ver el resultado en la consola:

```python
    print(validacionMensaje("SOS", "PELIGROSOS"))
```

Si quieres llamar a la función desde otro archivo es necesario hacer el import de la función:

```python
from src.main import validacionMensaje

print(validacionMensaje("SOS", "PELIGROSOS"))
```

Por último, si quieres escribir tus propios tests utilizando la librería unittest, debes importar tanto unittest como la función validacionMensaje. Luego, define una clase que herede de **unittest.TestCase** y dentro de ella crea métodos que comiencen con **test_**. Usa **self.assertTrue()** o **self.assertFalse()** para comprobar si el resultado de la función es el esperado:

```python
import unittest
from src.main import validacionMensaje

class TestValidacionMensaje(unittest.TestCase):
    def test_ejemplo(self):
        self.assertTrue(validacionMensaje("SOS", "PELIGROSOS"))
        self.assertFalse(validacionMensaje("RESCUE", "RSCU"))
```

## Cómo ejecutar los tests

Desde la raíz del proyecto se puede ejecutar los tests con el siguiente comando:

```bash
python -m unittest tests.test
```

Si se necesita ver el resultado de una forma más detallada de cada test se debe de añadir al comando el flag **-v**:

```bash
python -m unittest tests.test -v
```

También es posible ejecutar un único test, por si solo se quiere comprobar una parte específica de la función. Para ello, basta con añadir al comando el nombre de la clase de pruebas y el del método que se quiere comprobar:

```bash
python -m unittest tests.test.TestValidacionMensaje.test_mayusculas
```
