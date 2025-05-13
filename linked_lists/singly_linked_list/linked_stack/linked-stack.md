# Linked List Stack Implementation (LIFO)

## What is this structure?
This is a **Stack (LIFO)** implementation that internally uses a **linked list** for data storage.

## How does it work
- Behaves like any standard stack (Last-In-First-Out)
- Data is stored dynamically in memory through linked nodes
- **No resizing** needed - elements aren't moved, only pointers are modified

### Visual Representation

TOP (always points to newest)
↓
[newest] -> [node] -> [node] -> [oldest] -> null

## Performance Advantages
- **O(1) operations** for all stack methods:
  - `push()`: Add to head
  - `pop()`: Remove from head  
  - `top()`: Peek at head
- No wasted memory (dynamic allocation)
- No element shifting required

## What did i Learned
1. **Linked list mastery**: Reinforced understanding of node-based structures
2. **Stack mechanics**: Solidified LIFO principle and core operations
3. **Abstraction power**: Saw how to build higher-level structures using basic components

## Limitations and Improvements
 **Ideal for**: Unlimited-size stacks  
 **Not ideal for**: 
- Circular stacks (would need adaptation)
- Size-limited stacks 

**Implementation Note**:
The head pointer acts as the stack's top,
making all operations focus on one end for maximum efficiency.
