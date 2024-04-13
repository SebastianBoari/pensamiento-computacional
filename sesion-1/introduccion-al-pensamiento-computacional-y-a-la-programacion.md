# Introducción al Pensamiento Computacional y a la Programación

Si un nuevo Arquitecto llega a la obra de construcción y le pregunta al encargado de la obra si los cimientos se hicieron con zapatas corridas o pilotes encadenados, tanto uno como el otro pueden comunicarse sin entrar en mayores explicaciones.

En proyectos de sistemas entender y **compartir algunos términos y conceptos, con toda la carga de significado que conllevan, agiliza el diálogo y mejora la comprensión.**

Por eso, en todas las disciplinas se comparte un **Lenguaje Técnico** específico; y la Tecnología Informática, la Ing. de Software y la Programación de Sistemas en general, no son la excepción.


Haremos una primera introducción de ciertos conceptos, ideas y modelos que nos permitirá manejar un lenguaje común.

A lo largo del curso constantemente estaremos introduciendo conceptos porque las Ciencias de la Computación están en continuo cambio y renovación  

La Industria Informática colabora notablemente con el caos. **Emplea caprichosamente nombres o términos**, no siempre de acuerdo a su significado o peso específico, sino simplemente obedeciendo consignas de marketing.

Es importante entender qué significan los términos técnicos, por qué las ideas o modelos se llaman así y por qué se emplean es valioso para mantener el equilibrio.

*Aprender a programar o pensar como un programador no sólo implica conocer ciertos modelos, herramientas y técnicas, también es importante aprender a hablar como ellos*


## La computadora

### *¿Qué es una computadora?*

**Una computadora es un dispositivo físico de procesamiento de datos con propósito general.**

### *Entonces... ¿Qué es una computadora?*

¿El lavarropas que tiene programas y controla temperaturas y velocidad?

¿El teléfono celular que tiene el señor en el cajon que es a tapita y solo manda SMS, llamadas y jugar a la viborita?

¿El MP4 que ese que solo reproduce contenido multimedia?

Las respuesta a todas estas opciones es **NO**.

La idea de una computadora es que es capaz de procesar datos y obtener nueva información o resultados. 

*¿Cuáles datos? ¿Qué resultados? Los que se le pidan. ¿Quién le pide eso a la Computadora? El o los programas que está ejecutando.*

*¿Qué programas se pueden correr en una computadora? Lo que la imaginación de la tecnología vigente permita.* 

**Si tienes dudas acerca de si un dispositivo es una computadora; la pregunta que debes formularte es si puedes instalar una nueva app escrita por vos o descargada de internet. Si la respuesta es sí, entonces ¡califica como tal!**

## Software y Hardware

Toda computadora funciona con Software y Hardware. **El Software es el conjunto de herramientas abstractas (programas)**. Lo llamamos la componente lógica de un modelo computacional. Por otro lado, **el Hardware es el componente físico del dispositivo**. Es decir que, el Software dirá qué hacer y el Hardware lo hará.

**El mundo del Software** (Ingeniería de Software y Ciencias Básicas de la Computación) **es el mundo de las ideas, los modelos, el plano sin límites.** Casi todas las ideas novedosas que se ven en programación ya fueron pensadas varias décadas atrás. Pero suele tomar muchos años que una idea ingeniosa llegue al plano real porque **depende del grado de avance del Hardware**.

Hoy en día la tecnología de **Hardware dominante en computadoras es la electrónica**, pero no incluiría jamás a ésta en la definición de una computadora. **Las primeras computadoras no usaban esta tecnología.**

Los programadores elaboramos programas que serán ejecutados por una computadora, con su realidad y limitaciones de hardware. Usamos ideas ingeniosas, propias o ajenas, que sean viables, es decir, que nos permitan obtener resultados adecuados aplicándolas con el estado de avance tecnológico que disponemos.

## El modelo de Von Neumann y la Memoria Interna

**Arquitectura de una Computadora:** es el modelo que su diseño sigue con respecto a sus partes o subsistemas y la forma en que se interrelacionan. **La Arquitectura prevalente hoy en día es Von Neumann.** 

Un modelo de arquitectura Von Neumann consta de tres componentes o subsistemas a través de los cuales
fluye la información de una manera determinada:

1. La Información necesariamente ingresa a través del Subsistema de **Entrada - Salida (E/S)**. La entrada sería nuestro mouse o teclado y la salida, nuestra pantalla.

2. Todo dato que se necesite para el procesamiento debe alojarse en **Memoria Interna (MI)**, incluyendo los programas y los datos temporales que se generen.

3. La **Unidad Central de Proceso (UCP o CPU -Central Processing Unit-)** es quien realiza todas las transformaciones de datos, es decir, el proceso en sí. Los resultados se muestran a los usuarios a través del módulo **Entrada-Salida (E/S)**, pero éste los obtiene desde la **Memoria Interna (MI)**, por ello, los resultados que genera UCP son guardados en MI.

Una consecuencia directa del empleo de esta arquitectura es que una instrucción debe estar cargada en MI para ser ejecutada. Y como no resulta cómodo escribir, uno por uno, los comandos o sentencias, antes de ser ejecutados, en la programación moderna se trabaja con el concepto de **Programa Almacenado:**

**El Modelo de Funcionamiento de Programa Almacenado implica que para poder ser ejecutado un programa, debe ser cargado previamente en la memoria interna (MI).**

## El sistema Operativo

**El sistema operativo (SO) es el programa encargado de administrar el equipo y sus recursos**, que son constantemente disputados entre las solicitudes de todos los diferentes procesos o programas ejecutándose al mismo tiempo. Las computadoras modernas delegan esta gestión en el sistema operativo, siendo éste el
encargado de administrar el equipo.

Si bien una computadora puede funcionar sin sistema operativo muchas personas toman como un indicador de que un dispositivo puede considerarse una computadora si trabaja con un sistema operativo.


## Programa

Una definición tradicional podría ser:

**Un Programa de Computadora es un Algoritmo escrito en un Lenguaje de Programación.**

Resulta interesante una definición matemática de este concepto. Podemos decir que la Ecuación General de la Programación es la siguiente:

**P=A+D**

Un programa (P) es la suma de algoritmo (A) y datos (D).

Lo interesante de esta formulación es que podemos concluir rápida y genéricamente varias cosas, independientemente del programa del que se trate:

- Para escribir un **programa** es necesario escribir un **algoritmo** y diseñar una correcta organización de sus
**datos**. Los dos términos de la ecuación son igual de relevantes.

- Para mantener la misma calidad de P, si la calidad de D aumenta, A puede ser más simple. O, si mejoro A y D, forzosamente aumenta la calidad de P. Este concepto refleja mejor la idea de la programación
moderna.

Concluimos que: **Un buen programador no sólo mira el algoritmo, también debe ser muy
inteligente en la selección del modelo y las herramientas para organizar los datos.**

## Dato

Partamos de esta definición:

> “En el mundo de TI (tecnologías de la información), un dato es una representación simbólica ya sea numérica o alfabética, cuyo valor está listo para ser procesado por un ordenador y mostrarlo a un usuario en modo de información”

*Tomada de icorp.com.mx*

Seleccionamos esta definición porque incorpora el término **información**. En general, en software, diferenciamos dato de información considerando que **información es asignarle un significado al dato**.


## Algoritmo

**Un algoritmo es una serie finita de pasos precisos para alcanzar un objetivo.**

Un algoritmo debe constar de una
cantidad finita de pasos, de lo contrario sería imposible alcanzar el objetivo.

Recordemos que siempre el fin de un algoritmo es un objetivo bien específico.

Los pasos deben ser absolutamente precisos y claros para quién debe llevar a cabo el algoritmo.

A continuación detallaremos los
pasos que debemos seguir para escribir un algoritmo. 

1. Análisis del problema
2. Primer esbozo de solución
3. División del problema en partes
4. Ensamble de las partes

*¿De qué manera debe ser escrito el algoritmo para que lo comprenda la computadora?*

Es necesario precisar **qué entiende una computadora**. Hoy una computadora identifica y
discierne sólo dos eventos: **Presencia de Tensión** O **Ausencia de Tensión**. Estos estados son: disjuntos y
complementarios.

Es por esto que toda la realidad digital se modela empleando un sistema matemático binario (de base dos). 

La unidad mínima de medida de la información es un bit, corresponde a un dígito binario (0 o 1).

Tantos 0s y 1s es mucho,así que se agrupan (como decenas, centenas, etc., en el sistema decimal, pero en potencias de 2). 

Byte es 8 bits, 1 Kbyte es 1024 bytes, 1 MegaByte es 1024 Kbytes.

Es decir que **la computadora almacena y procesa información en forma de
unos y ceros**.

## Lenguaje de Programación

*¿Qué es un lenguaje?* 

**Un lenguaje es un protocolo de comunicación.**

*¿Y qué es un protocolo?*

**Un protocolo es un conjunto de normas consensuadas.**

Si logramos que un Lenguaje que pueda ser comprendido, tanto por el humano, como por la máquina, obtendremos lo que buscamos: una comunicación efectiva.

El primer lenguaje elegido era el que la máquina conocía, todo se expresaba con una colección de órdenes (primitivas) conocidas por el procesador y que llamamos **Lenguaje Assembler**.

Se hacia difícil trabajar en este lenguaje, había que salvar la distancia entre las dos puntas de la comunicación en un punto mas cercano a los humanos.

Un Lenguaje de Programación está dentro del grupo de los **Lenguajes Formales**. **Estos son lenguajes que tienen un conjunto acotado y definido de elementos válidos (tokens o palabras) y reglas de construcción específicas
de sentencias u oraciones válidas (reglas de sintaxis)**. Ejemplos de esta clase de lenguajes son los idiomas o Lenguas Vivas, el Lenguaje Matemático, el de Partituras Musicales, etc.

**Aún será necesario traducirle a la computadora esas órdenes en código máquina (assembler).** Un Lenguaje diseñado con todas las condiciones que hemos definido (formal, sin ambigüedades, acotado) facilita la traducción automática empleando **programas traductores**.


## Traductores

**Un lenguaje de programación con las características que definimos** previamente (formal, sin ambigüedades,
acotado), se identifica como un **Lenguaje de Alto Nivel**. **Un lenguaje como assembler, más cercano al código máquina**, se identifica como **Lenguaje de Bajo Nivel**.

Existen dos tipos de programas traductores: **Intérpretes o Compiladores**.

Con la técnica de **compilación**, se lee y posteriormente traduce completamente un programa y, sólo entonces, puede ser ejecutado.

Un **traductor intérprete** traduce sentencia a sentencia, a medida que se solicita su
ejecución. 

Los programas escritos en lenguaje de alto nivel se denominan **programas fuente** porque desde allí parten los traductores para generar una versión ejecutable.

Podemos editar un programa fuente con cualquier editor, por muy básico que sea. Una vez escrito y guardado, levantamos el programa fuente desde un programa intérprete para que gestione la traducción y ejecución del mismo.

Hay aplicaciones en las que nos ofrecen herramientas integradas con las que podemos trabajar durante todo el ciclo de vida de un programa (escribimos, probamos, corregimos, volvemos a probar, y así hasta que la versión
nos conforme y podamos liberarla).

Las aplicaciones que permiten hacer esto se denominan **Ambientes Centrados en Lenguajes o Entornos de Desarrollo**.

## Python

Es un lenguaje de alto nivel, interpretado, multi paradigma, multi plataforma.

- **Multi paradigma**: Se pueden construir programas con distintos enfoques o modelos de resolución de problemas usando el mismo lenguaje.

- **Multi plataforma**: Un programa en Python puede ejecutarse en distintos SO. 

- **Abierto**: Es decir que podemos ver el código de las herramientas que provee. 

> En esta sección el profesor nos señala que como consecuencia de ser "abierto", "de código abierto" u "open source" es "gratis". Este es un error común, lo único que podemos entender cuando nos señalen que un programa es de código abierto es que cualquier persona puede ver, modificar y distribuir el código fuente pero el uso del mismo puede ser de pago. Se suele llamar "Software Libre" cuando este en todos sus aspectos es libre hasta en su propio uso.

## Hola, Mundo!

¿Cómo escribimos un programa en Python que muestre por pantalla la frase Hola Mundo? (Tradicionalmente el primer programa que debe escribir todo programador).

| Programa              | Salida en pantalla |
|-----------------------|--------------------|
| print('Hola, Mundo!') | Hola mundo         |

Observemos que en el print() colocamos la frase dentro de los paréntesis. print() es una función y dentro de los paréntesis debemos colocar los parámetros de funcionamiento. En el caso de print(), qué queremos que muestre por pantalla.


```python
print('Hola, Mundo!')
```

La frase Hola Mundo la escribimos entre comillas simples. Siempre que queramos que se muestre texto constante (como en este caso, un cartel de salida) debe avisársele a Python que es un texto encerrándolo entre comillas simples o dobles (una u otra, no mezcladas). Sin embargo no veremos esas comillas en la salida, sólo veremos el texto deseado.

Vamos a escribir un programa que muestre la edad de Juan, que es 30:

```python
print('La edad de Juan es 30')
```

La salida en pantalla será

`La edad de Juan es 30`

Otra forma de hacerlo es así:

```python
oracion = 'La edad de Juan es 30'

print(oracion)
```
La salida en pantalla será

`La edad de Juan es 30`

¡Mismo resultado! Con esto ya podés comenzar con la guía de la Sesión 1.

A partir de la próxima clase comenzaremos a ensayar nuestros primeros programas un poco más complejos.