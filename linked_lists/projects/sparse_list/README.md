# Sparse List

- This project is from the book: Data Strucures and Algorithms in python.

## Description
An array A is sparse if most of its entries are emtpy. A list cab used to implement such an array efficiently.
In particular, for each nonempty cell A[i], we can store an entry (i, e) in L, where e is the element stored
at A[i]. This approach allows us to represent A using O(m) storage, where m is the number of nonempty entries
i A.

### Project
Provide such a SparseArray class that minimally supports methods __getitem__(i) and __setitem__(i, e) to
provide standard indexing operations. Analyze the effiency of these methods.


### Analize
The both __getitem__ and __setitem__ methods have a time complixity O(m) where m is the number of nonempty
elements in the array, the best case is when we wanted to do an operation at the beginning or at the end of
the array, with O(1) in both cases
