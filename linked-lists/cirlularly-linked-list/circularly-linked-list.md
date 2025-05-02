Que es esta estructura?
Es una Queue FIFO, pero internamente se manipulan los datos con una lista-enlazada-circular.

Como funciona?
en este tipo de lista, no hace falta tener una referencia al head ya que el tail apunta a este.
con esto podemos hacer que la lista se comporte igual que una LinkedQueue ya que todos los nodos forman un
circulo, entonces si se quiero acceder al primer nodo, solo hace falta ver al nodo que apunta el tail

a la hora de agregar un nuevo nodo, se le coloca como referencia siguiente al proximo nodo el actual "head",
y al tail se le coloca este nuevo nodo como referencia siguiente

esta estructura tambien nos permite hacer un comportamiento clave de las colas, el cual es la rotacion.
en vez de tener que eliminar y agregar elementos, lo unico que hacemos es mover el cualt tail las veces que
queramos rotar, de esta forma el elemento siguiente al acual tail sera el nuevo tail, y el siguiente sera
el nuevo head, y asi sucesivamente.

Que aprendi?
Con esto pude reforzar mas mi entendimiento sobre la estructura queue
asi como tambien mas control a la hora de visualizar los punteros
por ejemplo tambien, que pasa cuando solo queda un elemento y haces dequeue
si no tienes cuidado puede quedar tail apuntando a algo que ya no existe.


