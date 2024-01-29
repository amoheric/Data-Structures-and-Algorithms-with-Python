import random

# Define the hash functions

def basic_modulus_hash(value, table_size):
    """Basic Modulus Hash Function: Returns the remainder of value/table_size."""
    return value % table_size

def multiplicative_hash(value, table_size):
    """Multiplicative Hash Function: Multiplies value by a constant and mods by table_size."""
    constant = 0.6180339887  # A constant derived from the golden ratio
    return int(table_size * ((value * constant) % 1))

def folding_hash(value, table_size):
    """Folding Hash Function: Splits value into parts, sums them, and mods by table_size."""
    str_value = str(value)
    parts = [int(str_value[i:i+2]) for i in range(0, len(str_value), 2)]
    return sum(parts) % table_size

# Function to generate hash values for a given table size and hash function
def generate_hash_values(table_size, hash_function):
    # Generate random values
    random_values = [random.randint(0, 1000000) for _ in range(table_size)]

    # Apply hash function to each value
    hash_values = [hash_function(value, table_size) for value in random_values]

    return hash_values

# Table sizes
table_sizes = [1000, 10000, 100000]

# Generate hash values for each table size and hash function
hash_distributions = {}
for size in table_sizes:
    hash_distributions[size] = {
        "basic_modulus": generate_hash_values(size, basic_modulus_hash),
        "multiplicative": generate_hash_values(size, multiplicative_hash),
        "folding": generate_hash_values(size, folding_hash)
    }

hash_distributions[1000]  # Displaying results for table size 1000 as an example

