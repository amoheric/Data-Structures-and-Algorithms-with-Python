#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


// Define a simple hash function using modulo
unsigned int hashFunction1(unsigned int key, unsigned int tableSize) 
{

    return key % tableSize;

}

// Define a more complex hash function using bitwise operations
unsigned int hashFunction2(unsigned int key, unsigned int tableSize) 
{

    key = ((key >> 16) ^ key) * 0x45d9f3b;
    key = ((key >> 16) ^ key) * 0x45d9f3b;
    key = (key >> 16) ^ key;
    return key % tableSize;

}

// Define another hash function using multiplication and bit shifting
unsigned int hashFunction3(unsigned int key, unsigned int tableSize) 
{

    key = (key * 2654435761u) % tableSize;
    return key;

}

// Function to test the distribution of hash values
void testDistribution(unsigned int (*hashFunc)(unsigned int, unsigned int), unsigned int tableSize, unsigned int numValues) 
{

    vector<unsigned int> distribution(tableSize, 0);

    // Hash a range of values and record their distribution
    for (unsigned int i = 0; i < numValues; ++i) 
    {

        unsigned int hashedValue = hashFunc(i, tableSize);
        distribution[hashedValue]++;

    }

    // Calculate and display the distribution
    unsigned int min = *min_element(distribution.begin(), distribution.end());
    unsigned int max = *max_element(distribution.begin(), distribution.end());

    cout << "Hash Function Distribution (" << numValues << " values, Table Size " << tableSize << "):" << endl;
    cout << "Min: " << min << ", Max: " << max << endl;
    cout << "Average: " << static_cast<double>(numValues) / tableSize << endl;

}

int main() {
    const unsigned int sizes[] = { 1000, 10000, 100000 };

    for (unsigned int size : sizes) 
    {

        cout << "Testing with " << size << " values:" << endl;
        testDistribution(hashFunction1, size, size);
        testDistribution(hashFunction2, size, size);
        testDistribution(hashFunction3, size, size);
        cout << "----------------------------------------" << endl;

    }

    return 0;

}
