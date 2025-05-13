# Doubly Linked List Deque Implementation  

This structure is an implementation of a **Deque**, internally based on a **doubly linked list**.  

## How does it works  

- **Bidirectional Nodes**: Each node contains references to both the **previous** and **next** nodes.  
- **Sentinels**: Two special dummy nodes are added:  
  - **Header**: Marks the beginning of the list.  
  - **Trailer**: Marks the end of the list.  
  *(These nodes do not store actual data but simplify operations.)*  

### Advantages of Sentinels  
1. **Simplified Logic**: Always ensures a node exists before/after any real node, eliminating edge cases (e.g., empty list or single-node deletions).  
2. **Unified Operations**: Insertions/deletions follow the same steps regardless of position.  
3. **Circular Potential**: Enables easy circular list implementations.  

## Performance Benefits  
- **O(1) Operations**: All Deque operations (push/pop front/back) run in constant time—no array resizing needed.  
- **Solves SLL Limitations**: Overcomes issues like costly deletions in singly linked lists (SLLs).  

### What did i learned 
- Efficiently mimics a **Deque** with optimal time complexity.  
- Sentinels enable cleaner code and handle boundary cases seamlessly.  
