It's a FIFO Queue, but internally, the data is managed with a circular linked list.

How does it work?
In this type of list, you don’t need a reference to the head because the tail points to it.
This allows the list to behave the same way as a LinkedQueue, since all nodes form a circle. So, if you want to access the first node, you just need to look at the node that the tail points to.

When adding a new node:

- The new node’s next reference is set to the current head.

- The tail’s next reference is updated to this new node.

This structure also enables a key queue behavior: rotation.
Instead of having to remove and add elements, all we do is move the tail as many times as we want to rotate.
This way:

The element after the current tail becomes the new tail.

The next one becomes the new head, and so on.

What did I learn?
This reinforced my understanding of the Queue structure.

It also improved my ability to visualize pointers.

For example, what happens when only one element remains and you perform a dequeue?

If you’re not careful, the tail might end up pointing to something that no longer exists.
