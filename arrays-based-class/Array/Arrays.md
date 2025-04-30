== Arrays based DS in python == 

[[In python there are three arrays based data structures]].

- list
- tuple
- str

this three are widly use in python programs

important topics
 * Public behavior
 * inner workings


* Low-Level arrays
  First we have to understand a little of the computer memory
  
  the computer memory is composed by a large space of bits, this bits are grouped into larger units.
  this units typically are units of 8bits, called a byte. 8bits = 1byte
  
  to keep track of the information stored in the memory, the computer use an abstraction known as
  memory address, which is equivalent to the binary number of the sequential fashion
  
                     ---------------------------------------------------------------
 MEMORY ADDRESSES -> | 214 | 215 | 216 | 217 | 218  | 219 | 220 | 221 | 222  | 223 | 
                     ---------------------------------------------------------------
  
the computer hardware is designed in theory, so that any byte of the main memory can be accessed
based upon its memory address. Using asymtotic notation, wa say that any individual byte of memory
can be stored and retrieved in O(1) time.

A group of related variables can be stored one after another in a contigous portion of computer memory
we will denote such representation as an array

expample:

a text string is stored as an ordered sequence of inviduals characters.
python represents characters in the Unicode character set, and on most computing system, python 
internally represents each Unicode character with 16bits(2bytes)

so if we know that python represents Unicodes characters with 2bytes and we have a six-character string
"SAMPLE" it will be stored in 12 bytes of memory.
                      -------------------------------------------------------------
"SAMPLE' in MEMORY -> | 214|215 | 216|217 | 218|219 | 220|221 | 222|223 | 224|225 |
		      |    S    |    A    |    M    |    P    |    L    |    E    |
		      -------------------------------------------------------------
                           0         1         2         3         4         5

we will refer to each location of the array as a cell, and will use an integer idex to describe its
location within the array, for example, the cell of the array with index 4 has the character L and
is stored in bytes 222 and 223 of memory.

each cell of the memory must have the same size in bytes, this allows an arbitrary memory address 
to be accesed in constant time based on its index. if we know the memory address where the array starts
the number of bytes per element and the desired cell index within the array, the appropiate memory
address can be computed by the formula, start + cellsize * index, for example SAMPLE in index 4

start + cellzice * index
 214  + 2 * 4 = 222
 
when we have different zise objects and we want to stored them, python use an internal storage 
mechanism of an array of refference objects, that means that at the lowest level python stored a 
sequence of memory addresses at which the elements of the sequence reside
since each object has a different lenght of bytes will be impossible to know the location in memory
since we need the cellzise to calculate it. in this case python reserve a fixed number of bytes 
to each object address to 64-bits per address. In this way python can support constant-time access
to a list or tuple of different objects based on its index.

as the refferencial nature of the list in python, if we have a list of mutable objects and made a copy
this copy is a shallowcopy of the list, that means, the addresses stored in the new list are the same
stored in the old one so if we made a change to an object in the list, the object will has the same change in the old list

* Compact array in python
  a compact array in python is an array that stored the bits that represent the primary data
  (characters in the case of strings)
  
  the array object from array module allows you to create a compact array
  this class 
  
  this array class is based on arrays of the C programming language.
  
   ------------------------------------------------------
  | Code | C data type         | typical number of bytes |
  |------|---------------------|-------------------------|
  | 'b'  |  signed char        |            1            | 
  |------|---------------------|-------------------------|
  | 'B'  |  unsigned char      |            1            |
  |------|---------------------|-------------------------|
  | 'u'  |  Unicode char       |         2 or 4          |
  |------|---------------------|-------------------------|
  | 'h'  |  signed short int   |            2            |
  |------|---------------------|-------------------------|
  | 'H'  |  unsigned short int |            2            |
  |------|---------------------|-------------------------|
  | 'i'  |  signed int         |         2 or 4          |
  |------|---------------------|-------------------------|
  | 'I'  |  unsigned int       |         2 or 4          |
  |------|---------------------|-------------------------|
  | 'l'  |  signed long int    |            4            |
  |------|---------------------|-------------------------|
  | 'L'  |  unsigned long int  |           4             |
  |------|---------------------|-------------------------|
  | 'f'  |  float              |           4             |
  |------|---------------------|-------------------------|
  | 'd'  |  float              |           8             | 
   ------------------------------------------------------
  the array modul does not support for make compact arrays of user-defined data types


* Dynamic arrays and amortization
  A dynamic array is an array of certain value of bytes when the array is full filled the array asks
  for another fixed large array a so on
  

* Efficiency of python's sequence types

  Nonmutating behaviors
  
  those nonmutating behaviors of the list class are the same supported for the tuple class
 ---------------------------------- 
| Operation         | Running time |
|-------------------|--------------|
| len(data)         | O(1)         |
| data[j]           | O(1)         |
| data.count(value) | O(n)         |
| data.index(value) | O(k+1)       |
| value in data     | O(k+1)       |
| data1 == data2    | (k+1)        |
| data[j:k]         | O(k-j+1)     |
| data1 + data2     | O(n1 + n2)   |
| c * data          | O(cn)        |
 ----------------------------------
 
 Constant-time operations
 The length of an instance is returned in constant time because the class maintains such state information.
 The constant-time of syntax data[j] is assured by the underlying access into an array.
 
 Searching for values operations
 Each of the count, index, and __contains__ methods have to iterate the list from left to right
 so for the count method it has to iterate the complete instance to count every value if exists while
 for index and contains methods, they exit once they find the leftmost occurrence of the desired value if one exists.
 
 Creating new instances
 In all cases the result depends on the construction and initialization of the new result and therefore
 the asymptotic behavior is proportional to the length of the result.
 
 Mutating behaviors
 --------------------------------------------------------
|        Operation                        | Running time |
|--------------------------------------------------------|
|     data[j] = val                       | O(1)         |
|     data.append(value)                  | O(1)*        |
|     data.insert(k, value)               | O(n-k+1)*    |
|     data.pop()                          | O(1)*        |
|     data.pop(k), del data[k]            | O(n-k)       |
|     data.remove(value)                  | O(n)*        |
|     data.extend(data2), data += data2   | O(k-j+1)     |
|     data.reverses()                     | O(n)         |
|     data.sort()                         | O(nlogn)     |
 -------------------------------------------------------- 
 
list insert method amortized asymptotic notation
inserting items at the beginning of the list = Omega(n)
inserting items at the middle of the list = Omega(n)
inserting items at the end of the list = O(1)



Exercises.

* Reinforcement
- [[R-5.1]]
- [[R-5.2]]
- [[R-5.3]]
- [[R-5.4]] 
- [[R-5.5]]
