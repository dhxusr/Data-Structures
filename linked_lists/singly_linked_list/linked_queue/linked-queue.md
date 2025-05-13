# Linked List Queue Implementation (FIFO)

## What is this structure?
This is a **Queue (FIFO)** implementation that internally uses **linked nodes** for data manipulation.

## How does it work?
To simulate queue behavior, we leverage a key property of linked lists: 
- We maintain a reference to the **tail** (last element)

### Why focus on the tail?
In FIFO (First-In-First-Out) systems:
- The oldest element exits first
- If we added nodes at the **head**:

```
[new] -> [element] -> [element] -> [oldest] (tail)
```
- The oldest element would be at the tail
- No efficient way to remove the tail node in a linked list

### The Solution: Add at tail
By adding nodes at the **tail** instead:

```
 (head)                  (tail)
[first] -> [element] -> [element] -> [new]
```
- The oldest element stays at the **head**
- We can efficiently **remove from head** (O(1) operation)
- New elements are always **appended at the tail**

## What did i learned
1. **Linked list flexibility**: Demonstrated through this queue implementation.
2. **Queue mechanics**: Reinforced understanding of FIFO principles.
3. **Efficiency**: Achieved O(1) operations by strategically choosing insertion points.

**Implementation Note**:
This approach mirrors real-world queues (like waiting lines) where new entries join at the end while
service occurs at the front.
