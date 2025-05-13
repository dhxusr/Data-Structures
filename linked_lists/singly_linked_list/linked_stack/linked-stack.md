Qué es esta estructura?
Esta es una implementación de una pila (stack), pero que internamente funciona como una lista enlazada.

¿Qué significa eso? Que al usar la clase LinkedStack, se comporta como cualquier pila (LIFO),
pero los datos se almacenan dinámicamente en memoria mediante nodos enlazados.

Esto es interesante porque permite inserciones y eliminaciones rápidas y eficientes, sin necesidad de
redimensionar listas ni mover elementos, ya que solo se modifican punteros (especialmente en el nodo frontal).

¿Qué aprendí al implementarla?
Reforcé mi comprensión sobre listas enlazadas y cómo aplicar su estructura interna a otras abstracciones
como una pila.
También confirmé que entiendo bien el comportamiento y operaciones clave de una pila: push, pop, top.

¿Qué mejoraría?
Para una pila sin límite de almacenamiento, esta estructura es ideal.

Pero si se quisiera implementar una pila circular con límite, esta estructura no serviría tal cual,
y habría que adaptarla o elegir otra base (como un array circular o una lista doblemente enlazada).
