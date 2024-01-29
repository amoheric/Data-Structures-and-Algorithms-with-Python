#

#NAME: Eric Amoh Adjei
#DATE: 01/28/2024
#Assignment 3: Create your own Hash function



import random

# Defining the size of the hash tables
table_sizes = [1000, 10000, 100000]


# Hash Function 1: Simple Division Hash
def hash_function1(key, size):
    return key % size


# Hash Function 2: Multiplication Hash
def hash_function2(key, size):
    
    A = (5**0.5 - 1) / 2  # A constant (phi - 1) / 2
    return int(size * (key * A % 1))


# Hash Function 3: DJB2 Hash (a popular hash function)
def hash_function3(key, size):
    hash_value = 5381
    for char in str(key):
        
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value % size


# Function to generates a hash table and calculates distribution
def generate_and_analyze_hash_table(hash_function, size):
    hash_table = [0] * size
    for _ in range(size):
        
        key = random.randint(0, 1000000)  # Generates random keys
        index = hash_function(key, size)  # Gets the index from the hash function
        hash_table[index] += 1
        


    # Calculates distribution statistics
    max_value = max(hash_table)
    min_value = min(hash_table)
    avg_value = sum(hash_table) / size
    

    return max_value, min_value, avg_value


# Performs analysis for each hash function and table size
for size in table_sizes:
    print(f"Table Size: {size}")
    
    for i, hash_function in enumerate([hash_function1, hash_function2, hash_function3], start=1):
        max_value, min_value, avg_value = generate_and_analyze_hash_table(hash_function, size)
        print(f"Hash Function {i}:")
        print(f"   Maximum value in a slot: {max_value}")
        print(f"   Minimum value in a slot: {min_value}")
        print(f"   Average value in a slot: {avg_value}")
        
    print("=" * 40)

