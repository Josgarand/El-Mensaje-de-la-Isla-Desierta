# Análisis Técnico

## Complejidad Temporal (Big O)

- `m` es la longitud del `mensaje`
- `c` es la longitud del `cofre`

Dentro de la función `validacionMensaje` se hacen varias operaciones secuenciales sobre `mensaje` y `cofre`.

1. **Normalización (Se quitan los espacios y se pasa a minúsculas)**
   - Se utiliza `.replace()` y `.lower()`, funciones que recorren cada cadena de texto una vez.
   - Complejidad temporal: O(m + c)

2. **Validación con expresiones regulares**
   - `re.fullmatch()` también recorre una vez las cadenas de texto.
   - Complejidad temporal: O(m + c)

3. **Contadores con `collections.Counter`**
   - De la misma forma gracias a `collections.Counter` se recorren las cadenas de texto una vez y se crean los diccionarios de cuántas veces aparece cada carácter en `mensaje` y `cofre`.
   - Complejidad temporal: O(m + c)

4. **Comparación letra por letra**  
   - Se recorren todas las letras distintas del `mensaje`, y se comprueba las veces que aparece cada una en el `cofre`.
   - Acceder a un valor en un diccionario (`Counter`) sería O(1), así que este bucle es O(k), `k` es el número de letras distintas del mensaje, el número máximo que puede ser `k` es `k = m` si todas las letras del mensaje fuesen distintas.
   - Complejidad temporal: O(m)

Complejidad temporal:

**O(m + c)**  

---

## Complejidad Espacial (Memoria)

Se usan dos diccionarios para guardar que letras y cuanto se repiten en el mensaje y el cofre.

- Solo se permiten letras del alfabeto español con tildes, por lo tanto el número máximo de claves es **33** por cada diccionario (`m` y `c`), en términos de Big O se considera constante.

Complejidad espacial:  

**O(m + c)**

---

## Estructura de datos

- Para guardar las cadenas de texto del `mensaje` y `cofre` se utiliza **Counter**, transforma las cadenas de texto en diccionarios que indican cuántas veces aparece cada carácter, lo que facilita la comparación entre mensaje y cofre.

---

## Trade-offs

- **Simplicidad**: La función es clara y corta, gracias al uso de `Counter`.

- **Eficiencia**: Se logra una solución lineal O(m + c) usando estructuras adecuadas.

- **Validación con regex**: En un principio se filtraban estos caracteres que no eran válidos usando **ascii_lowercase** pero no funcionaba correctamente con las tildes, se cambió a **regex**, esto añade una pequeña sobrecarga pero se asegura de que no se introduzcan caracteres no válidos y permite diferenciar los caracteres que tienen tilde y de los que no.

- Los caracteres especiales no dan error pero siempre que estén en el mensaje o en el cofre el resultado de la función será "False".

---

## Casos extremos considerados

- Se ignora correctamente el uso de mayúsculas

- Se diferencia entre caracteres con tildes y los que no las tienen

- Funciona correctamente con cadenas de texto muy grandes por ejemplo de un millón de caracteres

- Se ignoran los espacios

- Cando se usan caracteres especiales ("#", "@", "€", etc...) no da error, da False
