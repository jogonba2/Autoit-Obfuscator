# OBFAU3 (Autoit-Obfuscator)
## Características del proceso de ofuscado

* Número de iteraciones del proceso de ofuscado.
* Enlazar includes desde otros ficheros del proyecto.
* Eliminar comentarios especificados por tags (comment-start/comment-end y cs/ce)
* Eliminar comentarios especificados por ;
* Eliminar comentarios especificados por #
* Eliminar regiones (#Region)
* Añadir nuevas regiones
* Ocultar nombres de variables
* Ocultar nombres de funciones
* Añadir funciones hardcodeadas especificadas en Hardcoded/HardcodedPrograms.py
* Añadir variables
* Añadir comentarios
* Añadir bloques de código generado al inicio
* Añadir bloques de código generado al final
* Añadir bloques de código generado entre lineas del código original.
* Añadir funciones
* Añadir llamadas a funciones
* Ocultar strings con método replace.
* Ocultar strings con método shuffle (genera codigo autoit para desordenar y ordenar las strings).
* Ocultar strings con método cipher  (medio implementado por problemas con la salida de los algoritmos de PyCrypto).
* Ocultar strings con método reverse.
* Ofuscar enteros.
* Añadir directivas, incluido #pragma compile con datos generados.
* Añadir espacios y tabuladores en el código.
* Añadir símbolos en el EOF.

## Características de los bloques de código generados 

* Generación de código y bloques If, For, Switch, Func y Simple (definiciones de nuevas variables haciendo uso de macros,constantes ofuscadas, funciones del lenguaje de aridades 0,1 y 2 y valores de tipos básicos)
* Definición del número mínimo y máximo de bloques a añadir.
* Definición del número mínimo y máximo de sentencias a añadir dentro del bloque (estas sentencias pueden ser a su vez nuevos bloques).
* Definición del número mínimo y máximo de condiciones lógicas a añadir en la guarda de los bloques generados.
* Definición del número mínimo y máximo de ElseIf dentro de un bloque If.
* Definición de la profundidad máxima de anidamiento de bloques generados.
* Definición de los valores mínimo y máximo de los enteros a usar en las definiciones (tiene sentido cuando se combina con la ofuscación de números).
* Posibilidad de añadir bloques al inicio, al final y entre medias del código original.
* Definición de la probabilidad de generación de nuevos bloques entre medias del código original.
* Definición del número mínimo y máximo de funciones a añadir.
* Definición de la aridad mínima y máxima de las funciones a añadir (define el número de parámetros de una función).
* Es necesario especificar todos estos valores en las tres posibilidades de adición de bloques (inicio,final,medio).

## Otras características

* Definición de la profundidad máxima en el ofuscado de enteros.
* Definición del tamaño en KB de la secuencia de símbolos a añadir tras el EOF.
* Variables declaradas con Local,  Dim y Global.
* Considerado Call en las llamadas a funciones. (Considerar que el usuario pueda desactivarlo)
* Considerado Assign en las definiciones de variables. (Considerar que el usuario pueda desactivarlo)
* Considerado Eval. (Considerar que el usuario pueda desactivarlo)
* Alterar nombres de las funciones y palabras clave de AutoIt (Considerar que el usuario pueda desactivarlo)
* Posibilidad de combinar los métodos de ofuscado de strings disponibles.
* Implementado operador ternario (parece funcionar solo con algunas versiones de AutoIt, dar posibilidad de activarlo)
* Todos los parámetros de los procesos son elegidos de forma aleatoria entre los valores límite especificados por el usuario (incrementa la dispersión y permite incrementar la exploración del espacio de soluciones si se emplean algoritmos genéticos para optimizar los parámetros).

 

## Futuras versiones

* Algoritmo genético para optimizar los parámetros del proceso.
* GUI (Sadfud y Blau)
* Compilar automáticamente con Aut2Exe y variar sus parámetros (compresión,  iconos,  ...)
* Añadir soporte de bloques While y Do Until.
* Considerar arrays.
* Considerar constantes y enumeraciones (const y enum). (Reparando bugs)
* Añadir expresiones lógicas siempre ciertas en el código ya existente
* Añadir más macros y funciones de autoit con más aridades.
* Considerar objetos.
* Considerar declaraciones relacionadas con objetos (With y For Inf)
* Añadir más funciones hardcodeadas.
* Añadir más métodos de ofuscado de strings.
* Parametrizar el script principal.
* Reordenación de código (tengo planteado algo usando grafos para tener en cuenta las dependencias).
* Dar la posibilidad de especificar más parámetros como el tamaño de los identificadores generados (esto se considera en las funciones implementadas pero no se deja al usuario especificarlo,   puede reducir considerablemente el tamaño del código).
* Hardcodear instancias simples de problemas NP.

Errores conocidos:

* Duplicate name (function) -> 
    * Problema: Repetición del nombre de alguna función.
    * Solución: Volver a ejecutar el ofuscador.
    
* Error in expresion        -> 
    * Problema: Error en algún Switch generado
    * Solución: Volver a ejecutar el ofuscador.
    
* Error subscripted array   -> 
    * Problema: Error general, fuente desconocida.
    * Solución: Volver a ejecutar el ofuscador, error general, fuente desconocida.

* Ante cualquier otro error, volver a ofuscar y si se soluciona (o no), comentad en Issues.
