# Análisis Técnico

## Complejidad Temporal (Big O)

- `m` es la longitud del `mensaje`
- `c` es la longitud del `cofre`

Dentro de la función `validacionMensaje` se hacen varias operaciones secuenciales sobre `mensaje` y `cofre`.

1. **Normalización (Se quitan los espacios y se pasa a minúsculas)**
   - Se utiliza `.replace()` y `.lower()`, funciones que recorren cada cadena de texto una vez.
   - Complejidad: O(m + c)

2. **Validación con expresiones regulares**
   - `re.fullmatch()` de la misma forma que las anteriores funciones recorren una vez las cadenas de texto.
   - Complejidad: O(m + c)

3. **Contadores con `collections.Counter`**
   - Recorre las cadenas de texto una vez para contar cada uno de los caracteres y crea los diccionarios de cuantas veces aparece cada caracter.
   - Complejidad: O(m + c)

4. **Comparación letra por letra**  
   - Se recorren las letras distintas en el `mensaje`, y por cada una se accede al número de veces que aparece en el `cofre`.
   - Acceder a un valor en un diccionario (`Counter`) es O(1), así que este bucle es O(k), donde `k` es el número de letras únicas del mensaje.
   - En el peor caso, `k = m` (si todas las letras del mensaje son diferentes).
   - → Complejidad: O(m)

Por tanto, la complejidad temporal de la función es:

**O(m + c)**  

---

## Complejidad Espacial (Memoria)

Se usan dos diccionarios (`Counter`) para almacenar las letras del mensaje y del cofre.

- En el peor caso, estos diccionarios tienen `m` y `c` entradas (si todas las letras son distintas).
- Solo se permiten letras del alfabeto español con tildes, por lo tanto el número máximo de claves es **33** por cada diccionario, en términos de Big O se considera constante.

Complejidad espacial:  

**O(m + c)**

---

## Estructura de datos

- Se utiliza **Counter** para transformar una cadena de texto en un diccionario que indica cuántas veces aparece cada carácter, lo que facilita la comparación entre mensaje y cofre.

---

## Trade-offs

- **Simplicidad**: La función es clara y corta, gracias al uso de `Counter`.

- **Eficiencia**: Se logra una solución lineal O(m + c) usando estructuras adecuadas.

- **Validación con regex**: En un principio se filtraban estos caracteres no validos con **ascii_lowercase** pero no funcionaba de forma correcta con las tildes, esto cambio a **regex** lo cual añade una pequeña sobrecarga, pero asegura que no se introduzcan caracteres no válidos.

- No es tolerante a caracteres especiales, no dará error pero siempre que esten en el mensaje o en el cofre el resultado será "False".

---

## Casos extremos considerados

- Se ignora el uso de mayúsculas

- Se diferencia entre caracteres con tildes

- Funciona correctamente con cadenas de texto muy grandes (de hasta un millón de caracteres)

- Se ignoran los espacios

- No da error cuando se usan caracteres especiales ("#", "@", "€", etc...)

