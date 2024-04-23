# Sentencias básicas y datos simples

**Tipos de datos, expresiones y funciones**

En esta sesión, vamos a trabajar tipos de datos simples, expresiones y funciones.

## Sentencias básicas

Ahora podemos centrarnos en la herramienta que vamos a emplear: Python, sobre cómo hacer un programa sencillo, cómo interactuar con el usuario, y más. ¿Estamos listos?


## Flujo de control de un programa

Para desarrollar un programa en Python escribiremos una colección de sentencias en orden de ejecución, de arriba hacia abajo; una en cada renglón, respetando la sintaxis de cada una. 

La secuencia en que las sentencias se ejecutan se llama Flujo de Control de un Programa (FCP, para nosotros , de ahora en más).

La ejecución de la primera a la última, una por una, es un Flujo de Control Estándar en Python. Es decir, que si el siguiente bloque fuese un programa de Python:


`Esto se ejecuta primero`

`Esto se ejecuta segundo`

`Esto se ejecuta tercero`

En este curso la comunicación de nuestros programas con el mundo exterior se realizará casi exclusivamente con el usuario; tanto sea para obtener datos de entrada, como para comunicarle resultados
parciales o finales.

## Funciones

Python dispone de herramientas tanto para poder hacer la lectura desde teclado (lo que el usuario tipea es enviado al programa), como para poder enviar resultados a la pantalla (para que el usuario pueda leerlos)

Para leer, o ingresar, o permitir que el usuario ingrese datos, usaremos la función **input()**.

Para mostrar toda la información que el programador considere debe mostrársele al usuario, emplearemos la
función **print()**

## Variables y Constantes

Los datos que nos ingresen o que el programa produzca y tengan que ser recordados o utilizados más adelante obligatoriamente serán alojados en la Memoria Interna (MI) y para hacerlo tendremos dos opciones:

**Constante**: Si el dato permanecerá inalterable, no cambiará de valor, entonces diremos que ese dato será una constante.

Para referenciar a una constante en un programa simplemente la llamamos por su valor.


| Declarar | Descripción                                     |
|----------|-------------------------------------------------|
|    2     | Es una constante numérica; y es el número **2** |
|  'Hola'  | Es un texto constante, la palabra **Hola**      |


> En realidad no existe una forma de declarar constantes en Python. En otros lenguajes de programación si intentamos cambiar el valor de una constante el lenguaje nos devolverá un error. En cambio python carece de este comportamiento así que lo que se suele hacer es nombrar las constantes en mayúsculas para indicarle al programador que la variable debería de ser tratada como una constante. 

```python
PI = 3.1416
```

**Variable:** Un dato puede cambiar o variar su valor, será una variable. No se puede emplear el mismo nombre para dos datos diferentes; una variable puede referenciar un sólo dato por vez.


 ```python
oracion = 'La edad de Juan es de 30 años'
```


## Buenas Prácticas de Programación

**Sobre convención de nombres:** 

Para nombres de variables y funciones, se usa snake_case, que es básicamente dejar todas las palabras en minúscula y unirlas con un guión bajo. 

Ejemplos:
numero_positivo, sumar_cinco, pedir_numero, etc.

Siempre emplear un nombre mnemotécnico, es decir que nos remita al significado que tendrá ese dato, siempre en snakecase: numero, letra, letra2, edad


**Variables:**

Las variables son cosas. Entonces sus nombres son sustantivos: nombre, numero, suma, resta,
resultado, respuesta_usuario. La única excepción son las variables booleanas (ya las vamos a ver, son aquellas que pueden guardar dos posibles valores: verdadero o falso), que suelen tener nombres como es_par, es_cero, es_entero, porque su valor es true o false.

A veces es útil alguna frase para identificar mejor el contenido: edad_mayor_hijo, apellido_conyuge

**Funciones**

Las funciones hacen algo. Entonces sus nombres son verbos en infinitivo. Se usan siempre verbos en infinitivo (terminan en -ar, -er, -i):

calcular_suma, imprimir_mensaje, correr_prueba, obtener_triplicado, etc.

De nuevo, las excepciones son las funciones que devuelven un valor booleano (V o F). Esas pueden llamarse como: es_par, da_cero,tiene_letra_a, porque devuelven verdadero o falso, y eso nos confirma o niega la afirmación que hace el nombre.

**Sobre ordenamiento de código:**

Cuando uno corre Python, lo que hace el lenguaje es leer línea a línea nuestro código. Lo que se puede ejecutar, lo ejecuta. Las funciones las guarda en memoria para poder usarlas luego.

Entonces es más ordenado y prolijo primero poner todas las funciones, y después el código
"ejecutable" (si van a dejar código suelto en el archivo).

## Tipos de Datos


### Datos Simples

Todos los Lenguajes disponen de un conjunto de tipos predefinidos de datos. ¿Qué significa que sean predefinidos? Que ya los conoce. Sabe cómo guardarlos en memoria y qué transformaciones puede aplicarles (operadores y contextos válidos).

| Tipo de dato       | Ejemplos de constantes                                              |
|--------------------|---------------------------------------------------------------------|
| entero - int       | 9 -5 37 0                                                           |
| real - float       | 0.01 88.72156333 -12.0 0.0                                          |
| complejo - complex | (10,9j) la componente con j del par indica la parte imaginaria      |
| lógico - bool      | True False (verdadero y falso)                                      |
| texto - str        | 'Ana y sus HERMANAS!, 7 en total' 'APRENDO A programar ****' 'u' '' |


El tipo str de Python permite trabajar con textos de 0, 1 o más caracteres. Debido a eso, en este lenguaje no diferenciamos mucho un carácter de un texto; ya que manipulamos un carácter como un texto de un único elemento.

La naturaleza de un texto es diferente a la de un número. Entonces, además de almacenarse internamente de manera distinta, trabajamos una string con sus propias reglas. Claramente no le haremos transformaciones matemáticas. Pero hay muchas transformaciones que se pueden y se necesitan realizar a textos. En general lo llamamos Edición de Texto. Las cadenas son un tipo de Secuencia. Una secuencia en Python es un conjunto contiguo de elementos con una organización interna. Cada carácter ocupa una posición determinada.

El texto: 'hola' no es igual a 'aloh' y tampoco a 'Holá'

## Operadores

Finalmente diremos que para transformar datos numéricos emplearemos operaciones válidas en Python, que en este caso serán coincidentes con operaciones matemáticas y de edición de texto.

A continuación una lista de **operadores aritméticos** válidos de Python:

| Símbolo |  Definición                    | Ejemplo        |
|---------|--------------------------------|----------------|
|   +     | Suma                           | 10+10          |
|   -     | Resta                          | 10-5           |
|   *     | Producto                       | 4*4            |
|   /     | División con Precisión Decimal | 5/2.5          |
|   //    | División Entera                | 8//2           |
|   %     | Resto                          | 10%2           |
|   +=    | Suma abreviada, agrega         | a=a+3 ≈ a+=3   |
|   -=    | Resta abreviada, quita         | a=a-3 ≈ a-=3   |
|   *=    | Producto abreviado             | a=a*3 ≈ a*=3   |
|   /=    | División abreviada             | a=a/3 ≈ a/=3   |
|   //=   | División entera abreviada      | a=a//3 ≈ a//=3 |
|   %=    | Resto abreviado                | a=a%3 ≈ a%=3   |


Para alterar cualquier precedencia debemos usar (), como en matemáticas

El orden de prioridad de ejecución va a ser:

1.  paréntesis ()
2. *, / , // , %
3. +, -

**Operadores de edición de texto** válidos:


| Símbolo      |  Definición                                                                  | Ejemplo                            |
|--------------|------------------------------------------------------------------------------|------------------------------------|
|   +          | Concatenación                                                                | 'Hola'  + 'Juan' --> 'HolaJuan'    |
|   *          | Repetición de texto                                                          | 'ja'*3 -> jajaja                   |
|   /          | División con Precisión Decimal                                               | 5/2.5                              |
| [k] o [-k]   | Selección de caracter                                                        | a='hola' a[0] -> h                 |
| [ i : j : p] | Selección de una porción del texto. Siendo: i : inicio, j : final, p : pasos | a[0:2]-> ho                        |
|   +=         | Concatenación abreviada                                                      | a = hola a+='y chau' -> holay chau |
|   *=         | Repetición abreviada                                                         | a*=2 -> holahola                   |


Para alterar cualquier precedencia debemos usar (), como en matemáticas

El orden de prioridad de ejecución va a ser:

4. paréntesis ()
5. corchetes []
6. +, *


## Manipulando Strings

Si bien esto lo vamos a ahondar en la siguiente Sesión de la materia, es importante saber que los strings,
como dijimos más arriba, son un conjunto de caracteres. 

Pero no sólo un conjunto, sino un conjunto ordenado. Cada carácter tiene una posición dentro de la palabra o string y no es lo mismo, por ejemplo:
CASA que SACA.

Cada caracter tiene una posición dentro del string, y las posiciones comienzan en cero, de izquierda a
derecha:

| 0     | 1     | 2     | 3     |
|-------|-------|-------|-------|
| **h** | **o** | **l** | **a** |

Por lo tanto, para la palabra “hola”, si quiero obtener el caracter 2, me devuelve la letra “L":

```python
palabra = 'hola'

print(palabra[2])
```


Pero no sólo puedo obtener los caracteres en las posiciones de la palabra, sino que puedo obtener slices o porciones de la palabra, usando algo que vemos por primera vez: **rangos**.

`[start : end : step]`

Un rango tiene 3 partes:

- **start** es desde dónde queremos que comience nuestra porción de la palabra

- **end** es hasta dónde queremos que llegue (ojo, no incluye a la misma posición)

- **step** es si queremos que se saltee posiciones (por ejemplo, que vaya de 2 en 2. Si no aclaramos un
step, va de 1 en 1.

Ejemplo:

```python
palabra = "pensamiento"

print(palabra[1:3])
```
Nos devolverá:

`en`

## Input y Casteos

Ya sabemos que Juan tiene 30 pero mejor si le preguntamos al usuario cuántos años tiene Juan en ese momento

```python
edad = input('Ingrese la edad de Juan: ')

print('La edad de Juan es: ', edad)
```

Primero nos devolverá por consola:

`Ingrese la edad de Juan: `

Una vez ingresemos el numero veremos en consola:

`La edad de Juan es: (el numero que hayamos ingresado)`

Notese como guardamos en la variable edad lo que le pedimos al usuario que ingrese.

**Intentemos hacerlo mas dinamico**

```python
nombreDinamico = input('Ingrese el nombre de usuario: ')

edadDinamica = input(f'Ingrese la edad de {nombreDinamico}: ')

print(f'La edad de {nombreDinamico} es de {edadDinamica} años')
```

Si probamos este código en python veremos que ya podemos mostrar en pantalla el nombre y edad de cualquier usuario.

También notamos una nueva forma de usar la funcion print() y mostrar texto alternando con variables.

## Imprimiendo Strings y Variables

El formato de un print es el siguiente: print paréntesis contenido paréntesis

El contenido puede ser:

- una variable
- un texto
- ambas, mezcladas.

También puedo mezclarlo de distintas formas. Estas son: usando +, usando comas, usando f"".

```python
dia_semana = 'domingo'
dia_mes =  14
```

**Usando el signo suma (+):**
```python
print("El día de la semana es: " + dia_semana)

print("El día del mes es: " + str(dia_mes))
```

**Usando coma (,):**
```python
print("El día de la semana es: ", dia_semana)

print("El día del mes es: ", str(dia_mes))
```

**Usando letra F y llaves (f"texto {variable})":**
```python
print(f"El día de la semana es: {dia_semana}")

print(f"El día del mes es: {str(dia_mes)}")
```
Son todas formas iguales de imprimir lo mismo. Pero, independientemente de cuál usemos, el formato siempre es el mismo: print paréntesis contenido paréntesis.

## Comentarios

En python si queremos comentar una linea para poder escribir texto anteponemos al texto el simbolo numeral (#) y luego escribimos.

Cada simbolo indica que la linea es un comentario, si saltamos a una linea inferior debemos volver a introducir otro simbolo para indicar que la nueva linea sigue siendo un comentario.

Ejemplo: 

```python
# Esto es un comentario
# Esto tambien es un comentario
```

**¿Para qué sirven los comentarios?**

Es buena comentar lo que hace una función o una porción de nuestro código. Asi es mas fácil y rápido para otra persona o para nosotros mismos entender cada porción de código.

Ejemplo:

```python
# Le pedimos al usuario que ingrese el año anterior
anio_anterior =  input('Ingrese el año anterior: ')

# Le mostramos al usuario cual es el año actual
print(f'El año actual es: {int(anio_anterior) + 1}')
```

Nótese que usamos la función int() para envolver la variable anio_anterior. 

La función int() convierte un tipo de dato cualquiera a un numero entero. Como el tipo de dato que guardamos en la variable es un string por ejemplo "2023" cuando sumemos + 1 para obtener el año actual veremos en consola "20231" porque python interpretara que es texto entonces hará una concatenación.

Al utilizar la función int() hacemos que la variable tome un valor de tipo entero pudiéndose hacer la suma correctamente.

## Funciones

Emplear funciones predefinidas o escritas por terceros es de gran ayuda. Imaginemos que cada vez que quisiéramos mostrar algo por pantalla tuviéramos que programar todo lo que la función print() hace.

Tiene razón Python en definir una función que hace el trabajo de mostrar datos en pantalla de forma genérica y los programadores sólo la usamos enviándole parámetros o argumentos para ajustar su funcionamiento a nuestras propias necesidades.


## Firma de la Función

Para definir una función propia en Python es necesario escribir una línea de encabezado y varias líneas de cuerpo. La línea de encabezado deberá comenzar con la palabra def seguida del nombre que le pondremos a nuestra función y luego paréntesis para terminar con dos puntos. A esta línea se le llama la firma de la función.

Ejemplo: 

```python
def unaFuncionCualquiera():
    # Cuerpo de la función
    print('Hola desde una función inventada por mi.')

    variableDentroDeLaFuncion = 'función'

    print(f'Esto es una {variableDentroDeLaFuncion}')
    # Fin del cuerpo de la función
```

## Devolviendo un resultado

Si queremos que la función devuelva un resultado será necesario elegir uno de los datos que maneja la función (sólo uno) y devolverlo a quién invocó a la función, empleando la sentencia return. Escribiremos
return y el dato.

Una sentencia return no sólo devuelve un dato, también determina la finalización de la ejecución de la función. Si no se coloca ningún return, la función no devuelve resultado y acaba su ejecución cuando el FCP termina de ejecutar el cuerpo.

Ejemplo:

```python
def suma(numero1, numero2):
    return numero1 + numero2

suma(5,6) # Devolverá 11

suma(10, 8) # Devolverá 18

suma(11, 24) # Devolverá 35
```
Pero para ver por pantalla el resultado podemos ver el valor que devuelve la función suma.

```python 
print(suma(5,6)) # Devolverá 11 y lo mostrará por pantalla
```
El return devuelve un valor cuando se invoca a la función.

El print lo manda a la pantalla, pero no devuelve nada.
