# Análisis Técnico

## Complejidad Temporal (Big O)

- Se tendrá en cuenta que `m` será la longitud del `mensaje` y `c` será la longitud del `cofre`

Dentro de la función `validacionMensaje` se hacen varias operaciones que se tienen en cuenta para la complejidad temporal.

1. **Normalización (Se quitan los espacios y se pasa a minúsculas)**
   - Se utiliza `.replace()` y `.lower()`, son métodos que recorren las cadenas de texto una vez.
   - Complejidad temporal: O(m + c)

2. **Validación con expresiones regulares**
   - Con el método `re.fullmatch()` también se recorrerá solo una vez las cadenas de texto.
   - Complejidad temporal: O(m + c)

3. **Contadores con `collections.Counter`**
   - De la misma forma `collections.Counter` recorre las cadenas de texto solo una vez creando diccionarios de estos caracteres.
   - Complejidad temporal: O(m + c)

4. **Comparación letra por letra**  
   - Se recorren todas las letras distintas del `mensaje`, y se comprueba las veces que aparece cada una en el `cofre`.
   - Acceder a un valor en un diccionario (`Counter`) sería O(1), así que este bucle es O(k), `k` es el número de caracteres distintos del mensaje, el máximo de caracteres que podrían existir es `k = m` si todas las letras del mensaje fueran distintas.
   - Complejidad temporal: O(m)

Complejidad temporal:

**O(m + c)**  

---

## Complejidad Espacial (Memoria)

Se usan dos diccionarios para guardar cuántas veces aparece cada carácter del mensaje y el cofre.

- Solo se permiten números y letras del alfabeto español incluidas con tilde, por lo tanto el número máximo de claves es **43** por cada diccionario, lo cual en términos de Big O se considera constante.

Complejidad espacial:  

**O(m + c)**

---

## Estructura de datos

- Para guardar las cadenas de texto del `mensaje` y `cofre` se utiliza **Counter**, el cual transforma las cadenas de texto en diccionarios que indican cuántas veces aparece cada carácter, lo que facilita la comparación entre mensaje y cofre.

---

## Trade-offs

- **Simplicidad**: La función fácil de entender y corta, gracias a utilizar los diccionarios hechos con `Counter`.

- **Eficiencia**: Se logra una solución lineal O(m + c) usando estructuras adecuadas.

- **Validación con regex**: En un principio se filtraban los caracteres que no eran válidos usando **ascii_lowercase** pero no funcionaba correctamente con las tildes, se cambió a **regex**, esto provoca una pequeña sobrecarga extra pero se asegura de que cuando se utilicen caracteres no válidos no de error y permite diferenciar los caracteres que tienen tilde de los que no.

- Los caracteres especiales no dan error pero siempre que estén en el mensaje o en el cofre el resultado de la función será "False".

---

## Casos extremos considerados

- Se ignora correctamente el uso de mayúsculas

- Se diferencia entre caracteres con tildes y los que no las tienen

- Funciona correctamente con cadenas de texto muy grandes por ejemplo, de un millón de caracteres

- Se ignoran los espacios

- Funciona correctamente con números

- Cuando se usan caracteres especiales ("#", "@", "€", etc...) no da error, devuelve False
