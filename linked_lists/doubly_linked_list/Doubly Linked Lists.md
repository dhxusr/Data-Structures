# Doubly Linked Lists

In a singly linked list, each node maintains a reference to the node that is immediately after it. We have demonstrated the usefulness of such a representation when managing a sequence of elements. 
However, there are limitations that stem from the asymmetry of a singly linked list. 

We emphasized that we can efficiently insert a node at either end of a singly linked list, and can delete a node at the head of a list, 
but we are unable to efficiently delete an arbitrary node from an interior position of the list because we cannot determine the node that immediately precedes the node to be deleted.

## Symmetric Structure

To provide greater symmetry, we define a linked list in which each node keeps:
- An explicit `next` reference to the node after it
- A `prev` reference to the node before it

Such a structure is known as a **doubly linked list**. These lists allow a greater variety of O(1)-time operations, including insertions and deletions at arbitrary positions within the list.

## Header and Trailer Sentinels

To avoid special cases when operating near the boundaries of a doubly linked list, we add special nodes at both ends:
- A **header** node at the beginning
- A **trailer** node at the end

These "dummy" nodes are known as **sentinels** (or guards), and they do not store elements of the primary sequence.

```

HEADER                                              TRAILER
     -----        -----        -----        -----        -----
    |     | <--> | JFK | <--> | PVD | <--> | SFO | <--> |     |
     -----        -----        -----        -----        -----

```

### Sentinel Initialization
- Empty list: 
  - Header's `next` points to trailer
  - Trailer's `prev` points to header
- Non-empty list:
  - Header's `next` points to first real element
  - Trailer's `prev` points to last real element

### Advantages of Sentinels
1. **Boundary consistency**: Header and trailer nodes never change
2. **Unified operations**: All insertions happen between existing nodes
3. **Safe deletions**: Every deleted node has neighbors on both sides

## Insertion Process

**Before insertion**:
`(a) [header] <--> [BWI] <--> [JFK] <--> [SFO] <--> [trailer]`

**After creating new node [PVD]**:

```
                                 <------->
(b) [header] <--> [BWI] <--> [JFK] [PVD] [SFO] <--> [trailer]
```
  
**After linking neighbors**:
`(c) [header] <--> [BWI] <--> [JFK] <--> [PVD] <--> [SFO] <--> [trailer]`

## Deletion Process
The deletion of a node, proceeds in the opposite fashion of an insertion. The two neighbors of the node to be
deleted are linked directly to each other, thereby bypassing the original node. As a result, that node will no
longer be considered part of the list and it can be reclaimed by the system. Because of our use of sentinels,
the same implementation can be used when deleting the first or the last element of a sequence, becuause even
such an element will be stored at a node that lies between two others.

**Before removal**:
`(a): [header] <--> [BWI] <--> [JFK] <--> [PVD] <--> [SFO] <--> [trailer]`

**After linking out [PVD]**:
`(c): [header] <--> [BWI] <--> [JFK] <--> [SFO] <--> [trailer]`

## Positional Abstraction

The greatest benefit of linked lists is O(1)-time operations at arbitrary positions when given a node reference. 

The **Positional List ADT** provides:
- A position as a stable marker within the list
- Position remains valid unless explicitly deleted
- Enables efficient sequence manipulation without element shifting

### Position Characteristics
- Unaffected by changes elsewhere in the list
- Only becomes invalid if explicitly deleted
- Serves as token for list location
