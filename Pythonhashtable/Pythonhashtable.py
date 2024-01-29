
#

#NAME: Eric Amoh Adjei
#DATE: 01/28/2024
#Assignment 3: Create your own Hash function

import random

# Define the hash functions

def basic_modulus_hash(value, table_size):
    """
    Basic Modulus Hash Function: Computes the hash value by taking the modulus of the value with the table size.
    This is a simple and common method in hash functions.
    
    Args:
    value (int): The value to be hashed.
    table_size (int): The size of the hash table.

    Returns:
    int: The computed hash value.
    """
    return value % table_size

def multiplicative_hash(value, table_size):
    """
    Multiplicative Hash Function: Multiplies the value by a constant, then takes the fractional part and multiplies by the table size.
    The constant is often chosen to be a fraction derived from an irrational number like the golden ratio.
    
    Args:
    value (int): The value to be hashed.
    table_size (int): The size of the hash table.

    Returns:
    int: The computed hash value.
    """
    constant = 0.6180339887  # A constant derived from the golden ratio
    return int(table_size * ((value * constant) % 1))

def folding_hash(value, table_size):
    """
    Folding Hash Function: Splits the value into equal-sized parts, adds them, and takes the modulus with the table size.
    This is useful for hashing values like strings or large numbers where different parts of the value contribute to the hash.
    
    Args:
    value (int): The value to be hashed.
    table_size (int): The size of the hash table.

    Returns:
    int: The computed hash value.
    """
    str_value = str(value)
    parts = [int(str_value[i:i+2]) for i in range(0, len(str_value), 2)]
    return sum(parts) % table_size

# Function to generate hash values for a given table size and hash function
def generate_hash_values(table_size, hash_function):
    """
    Generates a list of hash values by applying the hash function to randomly generated values.

    Args:
    table_size (int): The size of the hash table.
    hash_function (callable): The hash function to be used.

    Returns:
    list: A list of hash values.
    """
    # Generate random values
    random_values = [random.randint(0, 1000000) for _ in range(table_size)]

    # Apply hash function to each value
    hash_values = [hash_function(value, table_size) for value in random_values]

    return hash_values

# Function to analyze the distribution of hash values
def analyze_distribution(hash_values):
    """
    Analyzes the distribution of hash values by counting the number of unique values and collisions.

    Args:
    hash_values (list): A list of hash values.

    Returns:
    tuple: A tuple containing the number of unique values and the number of collisions.
    """
    unique_values = len(set(hash_values))
    total_values = len(hash_values)
    collisions = total_values - unique_values
    return unique_values, collisions

# Main execution: Apply hash functions and analyze distributions
table_sizes = [1000, 10000, 100000]
hash_distributions = {}

for size in table_sizes:
    hash_distributions[size] = {
        "basic_modulus": generate_hash_values(size, basic_modulus_hash),
        "multiplicative": generate_hash_values(size, multiplicative_hash),
        "folding": generate_hash_values(size, folding_hash)
    }

# Analyze distributions for each table size and hash function
analysis_results = {}

for size in table_sizes:
    analysis_results[size] = {}
    for hash_function in hash_distributions[size]:
        unique_values, collisions = analyze_distribution(hash_distributions[size][hash_function])
        analysis_results[size][hash_function] = {
            "unique_values": unique_values,
            "collisions": collisions
        }

# Print the analysis results
for size in analysis_results:
    print(f"Table Size: {size}")
    for function in analysis_results[size]:
        print(f"  {function}: Unique Values: {analysis_results[size][function]['unique_values']}, Collisions: {analysis_results[size][function]['collisions']}")
