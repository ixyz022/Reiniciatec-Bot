# Tareas de Programación del Robot MBot2

El siguiente documento tiene como objetivo registrar las tareas de programación asignadas a cada persona, así como los objetivos generales del equipo y enlaces de interés para acceder a la documentación del robot.

## Contexto

El siguiente texto tiene por objeto dejar constancia de las tareas de programación y destinar cada una de las subrutinas (le llamamos subrutinas a pequeñas acciones del robot que pueden ser reutilizables en una función en la programación) a una persona para ser programada. Así todos van ganando expertise en la programación del robot, que será necesaria para poder resolver dudas a la hora de hacer los bootcamps, y a la hora de destinarlos como mentores de los equipos que participarán en las competencias.

## Links de interés

La documentación del robot se encuentra en los siguientes enlaces:

- [APIs for CyberPi](https://education.makeblock.com/help/mblock-python-editor-python-api-documentation-for-cyberpi/)
- [APIs for mBuild Modules](https://education.makeblock.com/help/mblock-python-editor-apis-for-mbuild-modules)
- [APIs for Extension Boards](https://education.makeblock.com/help/mblock-python-editor-apis-for-extension-boards)
- [APIs for Function Extension](https://education.makeblock.com/help/mblock-python-editor-apis-for-function-extension)

La documentación está en inglés, pero estamos trabajando en una traducción. Sin embargo, para el momento en que esté lista, necesitamos que todos ya estén más o menos habituados con la programación del robot.

## Objetivos generales

- Que todos los miembros del equipo tengan experiencia práctica en la programación del robot mBot2, tanto en bloque como en Python.
- Que todos los mentores puedan resolver dudas básicas y medias sobre la programación y la estructura del robot.
- Que todos los mentores puedan experimentar con el robot, de modo de encontrar nuevas funcionalidades, formas o habilidades del robot.

## Subrutinas a ser programadas

1. Realizar una correcta detección de un color para posteriormente realizar una secuencia de funcionalidades a partir del color detectado.
2. Permitir que al menos dos servos funcionen de manera simultánea utilizando la asincronicidad. Por ejemplo:
   - El servo de agarre se cierre mientras mueve el brazo.
   - El servo de la cabeza gire mientras el brazo se mueve.
3. Que el robot pueda seguir líneas mientras realiza otra acción.

4. Estandarizar un método para optimizar la funcionalidad del movimiento correcto del robot, que permita mayores usos de reutilización. Por ejemplo:
   - Que permita bailar y moverse al mismo tiempo.
   - Que funcione para seguir las líneas y movimientos fuera de las líneas.
   - Permitir que un servo se pueda mover de forma correcta y natural de forma lenta.
5. Para un mayor control de las prácticas con el robot, se necesita que NO sea necesario apagar o "cargar" un nuevo código en el robot en cada instancia, es decir, que exista una forma alternativa de terminar a la fuerza con cualquier acción que está realizando el robot por medio de un botón X.
6. Las luces LEDs pertenecientes a los ojos del robot disponen de varias características que hasta el momento han sido poco aprovechadas. Encuentre nuevas formas de implementarlos de diferentes maneras, considerando que no sean similares a "presentaciones" anteriores.

¡Buena suerte en la programación del robot mBot2!

