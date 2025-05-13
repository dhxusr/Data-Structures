Que es esta estructura?
Es una cola (FIFO) pero la forma en la que se manipulan los datos desde dentro es con nodos enlazados.

Como funciona?
En este caso, para simular el comportamiento de una cola, podemos aprovecharnos de una propiedad de las listas
enlazadas y es que se guarda referencia de su ultimo elemento, Por que hago mencion al ultimo elemento?
ya que el comportamiento FIFO se basa en que el elemento con mas tiempo es el que sale primero si
enlazamos los nodos(agregamos datos) al head de la lista, el elemento mas viejo va a estar en el ultimo
nodo, y no hay forma eficiente para eliminar ese ultimo nodo usando una lista enlazada, lo que si podemos hacer
es agregar nodos al final de la lista, con la referencia de tail, esto nos permite que el elemento mas viejo
sea el referente del head, osea el primer nodo de la lista, el cual si podemos eliminar de forma eficiente.
entonces se puede ver como agregar los datos a la derecha de la lista, en vez de a la izquierda.

agregar elementos a la izquierda

            HEAD                                 TAIL
[nuevo] -> [elemento]->[elemento]->[elemento]->[primero]


agregar elementos a la derecha

 HEAD                                TAIL
[primero]->[elemento]->[elemento]->[elemento] -> [nuevo]

Este enfoque nos permite simular el comportamiento de una cola de forma eficiente.

Que aprendi?
Al implementar esta estructura, pude ver la flexibilidad de una lista enlazada.
reforze mas mi entendimiento sobre las colas.

