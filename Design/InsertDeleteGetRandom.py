class RandomizedSet:


    """A combination of hash table and array can be used as hash table will help to perform insert , delete in O(1), swap the value to be deleted with the 
    last element in the array for O(1) deletion from array as well. Finally, an array can be used for O(1) random. Hash tables are not indexed so can't be used for 
    generating random numbers as random numbers are generated by choosing a random number from the index of the list and then retrieving the number at that index"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash:
            return False
        else:
            self.hash[val] = len(self.array)
            self.array.append(val)
            return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash:
            return False
        else:
            index_val = self.hash[val]
            self.array[index_val] = self.array[-1]
            self.hash[self.array[index_val]] = index_val

            
            del self.hash[val]
            self.array.pop()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)