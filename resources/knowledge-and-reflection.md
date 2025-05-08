# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> The main commonality all of these functions have is that they obscure the original value of the input using a key  
> They also provide an output in a fixed range and attempt to evenly distribute values.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> SSH  
> __Pro:__
> very very simple.  
> __Con:__
> Every key collides.  
> 
> sum_of_ascii_values  
> __Pro:__
> easy and fast to both understand and compute  
> __Con:__
> poor distribution with similar values
> 
> pearson_hash  
> __Pro:__
> more resistant to collisions  
> __Con:__
> slow. complex implementation
> 
> python's built-in hash  
> __Pro:__
> fast  
> __Con:__
> not consistent without a fixed seed value
> 
> SHA256  
> __Pro:__
> very good at resisting collisions; quite sensitive to changes in the input  
> __Con:__
> it's slow and honestly kinda overkill for this


3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> uniform distribution: prevents too many values in the same area  
> determinism: ensuring the same value always returns the same location
> time efficiency: keeps the hashmap fast which was the whole purpose of implementing it

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I'd choose to use a sum of ascii values hash for this assessment. due to the lack of required security in the scenario and my belief that it would be faster than having to import hashlib for sha256.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> initialise value to return. using a constant starting point keeps determinism high
> ```python
> hash_ = 0
> ```
> this process mixes up the input with ascii values, a XOR and a lookup in the pearson table.  
> the high volitility for change in the output from a small key change helps with input sensitivity. it also promotes a uniform output
> ```python
> for char in key:
> hash_ = pearson_table[hash_ ^ ord(char)]
> ```
> compress result to a space in the table using the remainder. this random output should distribute things evenly keeping it more resistant to collisions
> ```python
> return hash_ % SIZE
> ```

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> ```python
> hashmap[player.id] = player
> ```
>  
>  hashmap's __setitem__ hashes a player's ID and chooses a player list which the player is then inserted.  
> (at the head unless provided a value to say insert at tail)

## Reflection

1. What was the most challenging aspect of this task?

> dealing with having the option of using both string keys and player object keys. debugging the program due to errors that introduced was annoying

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> I liked the use of PlayerList and in any other language id do the same. but in python, I'd use the built-in list with tuples inside

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
