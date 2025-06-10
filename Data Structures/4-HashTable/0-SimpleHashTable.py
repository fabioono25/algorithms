# Data Structures/4-HashTable/0-SimpleHashTable.py
# Problem: Implement a simple HashTable from scratch.
# This will include basic hash function, collision handling (chaining),
# and operations like put, get, remove.

# --- Simple Solution: Basic HashTable with Chaining ---
class SimpleHashTableChaining:
    """
    A simple HashTable implementation using chaining for collision resolution.
    - Hash function: Basic modulo operator.
    - Storage: A list of lists (buckets), where each inner list stores (key, value) pairs.
    """
    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("HashTable size must be positive")
        self.size = size
        self.buckets = [[] for _ in range(self.size)] # List of empty lists (chains)

    def _hash_function(self, key) -> int:
        """Simple hash function: uses hash() built-in and modulo operator."""
        # hash() can return negative values, abs() ensures positive before modulo
        return abs(hash(key)) % self.size

    def put(self, key, value) -> None:
        """Adds a key-value pair to the hash table. Handles collisions by chaining."""
        bucket_index = self._hash_function(key)
        bucket = self.buckets[bucket_index]

        # Check if key already exists in the chain and update it
        for i, (k_existing, v_existing) in enumerate(bucket):
            if k_existing == key:
                bucket[i] = (key, value) # Update existing key
                return

        # If key not found, append new key-value pair to the chain
        bucket.append((key, value))

    def get(self, key):
        """Retrieves the value associated with a key. Returns None if key not found."""
        bucket_index = self._hash_function(key)
        bucket = self.buckets[bucket_index]

        for k_existing, v_existing in bucket:
            if k_existing == key:
                return v_existing
        return None # Key not found

    def remove(self, key) -> bool:
        """Removes a key-value pair from the hash table. Returns True if successful, False otherwise."""
        bucket_index = self._hash_function(key)
        bucket = self.buckets[bucket_index]

        for i, (k_existing, v_existing) in enumerate(bucket):
            if k_existing == key:
                bucket.pop(i) # Remove the (key, value) pair
                return True
        return False # Key not found

    def __str__(self):
        # Helper to visualize the HashTable
        representation = []
        for i, bucket in enumerate(self.buckets):
            representation.append(f"Bucket {i}: {bucket}")
        return "\n".join(representation)

# --- Robust Solution: HashTable with Resizing and Load Factor ---
class RobustHashTableChaining(SimpleHashTableChaining): # Inherits from Simple for _hash_function
    """
    Extends SimpleHashTableChaining with:
    - Dynamic resizing when load factor exceeds a threshold.
    - Slightly improved hash function consideration (though still basic).
    - Tracks element count and load factor.
    """
    DEFAULT_INITIAL_SIZE = 8
    DEFAULT_LOAD_FACTOR_THRESHOLD = 0.75

    def __init__(self, initial_size=DEFAULT_INITIAL_SIZE, load_factor_threshold=DEFAULT_LOAD_FACTOR_THRESHOLD):
        if initial_size <= 0:
            raise ValueError("HashTable initial size must be positive")
        super().__init__(size=initial_size) # Calls SimpleHashTableChaining.__init__
        self.load_factor_threshold = load_factor_threshold
        self.num_elements = 0

    def _calculate_load_factor(self) -> float:
        return self.num_elements / self.size

    def _resize(self, new_size: int) -> None:
        """Resizes the hash table to new_size and rehashes all existing elements."""
        old_buckets = self.buckets
        self.size = new_size
        self.buckets = [[] for _ in range(self.size)]
        self.num_elements = 0 # Reset, will be recounted during re-put

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value) # Re-put elements into the new, resized table

    def put(self, key, value) -> None:
        """Adds a key-value pair, checking for resize before adding."""
        bucket_index = self._hash_function(key)
        bucket = self.buckets[bucket_index]

        key_exists = False
        for i, (k_existing, v_existing) in enumerate(bucket):
            if k_existing == key:
                bucket[i] = (key, value) # Update existing key
                key_exists = True
                break # No change in num_elements or need to check load factor

        if not key_exists:
            bucket.append((key, value))
            self.num_elements += 1
            if self._calculate_load_factor() > self.load_factor_threshold:
                self._resize(self.size * 2) # Double the size

    def remove(self, key) -> bool:
        """Removes a key-value pair. Updates num_elements."""
        # Note: Could also consider shrinking the table if load factor gets too low,
        # but this is often omitted for simplicity in basic implementations.
        removed = super().remove(key) # Call SimpleHashTableChaining's remove
        if removed:
            self.num_elements -= 1
        return removed

# --- Jedi Solution: Discussion of Advanced Concepts ---
# (This section is primarily comments)

# **1. Hash Functions:**
#    - The choice of hash function is critical for performance. A good hash function
#      distributes keys uniformly across buckets, minimizing collisions.
#    - `hash(key) % self.size` is very basic. Issues:
#        - `hash()` in Python can have different sequences for strings between runs for security.
#        - Poor distribution if `size` has common factors with many hash codes.
#        - Often, prime numbers are preferred for table sizes to help with distribution.
#    - Cryptographic hashes (MD5, SHA-1) can be used for very good distribution but are slower.
#    - For custom objects, implementing `__hash__` and `__eq__` methods correctly is essential.

# **2. Collision Resolution Strategies:**
#    - **Chaining (used above):** Each bucket is a list (or linked list) of items that hash
#      to the same index. Simple to implement. Performance degrades to O(N) in worst case
#      (all keys hash to same bucket) but averages O(1 + alpha) where alpha is load factor.
#    - **Open Addressing:** All items are stored within the bucket array itself.
#      When a collision occurs, "probe" for the next empty slot.
#        - **Linear Probing:** Check `(hash(key) + i) % size`. Suffers from primary clustering.
#        - **Quadratic Probing:** Check `(hash(key) + i*i) % size`. Reduces primary clustering but
#          can cause secondary clustering and may not find an empty slot if table is > half full.
#        - **Double Hashing:** Use a second hash function to determine probe step:
#          `(hash1(key) + i * hash2(key)) % size`. Can give good distribution.
#      Open addressing can be faster due to better cache performance (no pointer chasing)
#      but requires careful handling of deletions (e.g., using tombstones) and resizing.

# **3. Load Factor and Resizing:**
#    - Load Factor (alpha) = num_elements / table_size.
#    - Keeping alpha low (e.g., < 0.7-0.8 for chaining, < 0.5 for open addressing) is key
#      to maintaining O(1) average performance.
#    - Resizing (rehashing) is an O(N+M) operation (N elements, M new table size) but amortized
#      over many insertions, it contributes O(1) to each insertion on average.

# **4. Python's `dict` and `set`:**
#    - Python's built-in `dict` (and `set`, which uses a similar underlying hash table) is highly
#      optimized, implemented in C.
#    - It uses a sophisticated open addressing scheme (variant of quadratic probing with
#      randomization) and carefully tuned resizing.
#    - For most practical purposes, always use Python's `dict` and `set`. Implementing
#      a hash table from scratch is an educational exercise.

# --- Example Usage ---
if __name__ == "__main__":
    print("--- SimpleHashTableChaining ---")
    ht_simple = SimpleHashTableChaining(size=5)
    ht_simple.put("apple", 10)
    ht_simple.put("banana", 20)
    ht_simple.put("cherry", 30) # Potential collision if hash("apple") % 5 == hash("cherry") % 5
    ht_simple.put("date", 40)
    ht_simple.put("elderberry", 50)
    ht_simple.put("fig", 60) # Likely collision, will extend a chain

    print(ht_simple)
    print(f"Get 'banana': {ht_simple.get('banana')}")  # Expected: 20
    print(f"Get 'grape' (non-existent): {ht_simple.get('grape')}") # Expected: None
    ht_simple.put("apple", 15) # Update apple
    print(f"Get 'apple' (updated): {ht_simple.get('apple')}") # Expected: 15
    ht_simple.remove("date")
    print(f"Get 'date' (removed): {ht_simple.get('date')}") # Expected: None
    print("After removals/updates:")
    print(ht_simple)

    print("\n--- RobustHashTableChaining (with Resizing) ---")
    ht_robust = RobustHashTableChaining(initial_size=3, load_factor_threshold=0.7)
    print(f"Initial size: {ht_robust.size}")
    ht_robust.put("one", 1)
    print(f"Size after 1 put: {ht_robust.size}, Elements: {ht_robust.num_elements}")
    print(ht_robust)
    ht_robust.put("two", 2)
    print(f"Size after 2 puts: {ht_robust.size}, Elements: {ht_robust.num_elements}") # Should resize if 2/3 > 0.7
    print(ht_robust)
    ht_robust.put("three", 3)
    print(f"Size after 3 puts: {ht_robust.size}, Elements: {ht_robust.num_elements}") # Should resize if 3/new_size > 0.7
    print(ht_robust)
    ht_robust.put("four", 4)
    print(f"Size after 4 puts: {ht_robust.size}, Elements: {ht_robust.num_elements}")
    print(ht_robust)

    print(f"Get 'two': {ht_robust.get('two')}") # Expected: 2
    ht_robust.remove("three")
    print(f"Elements after removing 'three': {ht_robust.num_elements}")
    print(f"Get 'three' (removed): {ht_robust.get('three')}") # Expected: None
    print(ht_robust)

    print("\n--- Jedi Solution (Discussion) ---")
    print("See comments in the Jedi Solution section for details on advanced concepts.")
    # Example of Python's dict
    py_dict = {}
    py_dict["key1"] = "value1"
    py_dict["key2"] = "value2"
    print(f"Python dict: {py_dict}, Get 'key1': {py_dict.get('key1')}")
