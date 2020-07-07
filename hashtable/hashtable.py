class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [[] for i in range(self.capacity)]


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # This needs to be changed because of the lists now
        # return sum(x is not None for x in self.storage)
        return len([x for x in self.storage if x])/len(self.storage)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # These values are for 64-bit implementation
        hash_val = 0xcbf29ce484222325
        FNV_prime = 0x100000001b3

        # Default encoding is UTF-8
        encoded = key.encode()

        # Adjust value of address for key
        for char in encoded:
            hash_val = hash_val * FNV_prime
            hash_val = hash_val ^ char

        return hash_val


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Get the hash index and then store the given value there
        hash_ind = self.hash_index(key)

        # Flag for if key already exists
        exists = False

        # Check if the list at index is empty
        if not self.storage[hash_ind]:
            # Append the new key and value as a tuple into the list stored at that index
            self.storage[hash_ind].append((key, value))
        # Else, check if key already exists in list
        else:
            for i, tup in enumerate(self.storage[hash_ind]):
                if tup[0] == key:
                    # Replace that tuple with new tuple
                    self.storage[hash_ind][i] = ((key, value))
                    exists = True
                    break
            # If the list wasn't empty and didn't find the key, add it
            if not exists:
                self.storage[hash_ind].append((key, value))
        
        # Check load factor after adding a value
        if self.get_load_factor() > 0.7:  # If it's getting crowded
            self.resize(self.capacity*2)  # Double the capacity





    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # If there is a value stored at the hash index replace with None
        hash_ind = self.hash_index(key)

        # Flag for if key found
        existed = False

        # Check if the list at that index is not empty
        if self.storage[hash_ind]:
            # Loop through tuples to matching key
            for i, tup in enumerate(self.storage[hash_ind]):
                # If key found, delete tuple at that index
                if tup[0] == key:
                    del self.storage[hash_ind][i]
                    existed = True
                    break
        # If loop completed without finding key, print error
        if not existed:
            # return None
            print('Key not found', key)

        # if not self.storage[hash_ind]:
        #     print("Key not found")
        # else:
        #     self.storage[hash_ind] = None

        # Check load factor after deleting an item
        if (self.get_load_factor() < 0.2):  # If it's getting sparse
            new_min = self.capacity//2  # Half the capacity
            if new_min < 8:
                new_min = 8  # Lowest it can get is 8
            self.resize(new_min)  


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Return the value stored at the hash index
        hash_ind = self.hash_index(key)

        # Check if the list at that index is not empty
        if self.storage[hash_ind]:
            # If it's not empty check through tuples for matching key and return the value
            for tup in self.storage[hash_ind]:
                if tup[0] == key:
                    return tup[1]
        # If key does not exist then return None
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Storage list for current hash table values
        temp_storage = []

        # Loop through old hash table
        for i in range(len(self.storage)):
            # For each non-empty list loop through to get key and value
            if self.storage[i]:
                for tup in self.storage[i]:
                    # Put key, value tuple in the storage list
                    temp_storage.append((tup[0], tup[1]))
        
        # Recreate hash table with new capacity and empty lists
        self.capacity = new_capacity
        self.storage = [[] for i in range(self.capacity)]

        # Refill hash table with stored values
        for tup in temp_storage:
            self.put(tup[0], tup[1])




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    print(ht.get_load_factor())
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    print(ht.get_load_factor())
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    print(ht.get_load_factor())
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
