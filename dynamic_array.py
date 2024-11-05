class DynamicArray:
    def __init__(self):
        # Start with capacity of 1, like a C++ vector
        self.capacity = 1
        self.size = 0
        # Create initial array filled with zeros (C-style array)
        self.arr = [0] * self.capacity

    def push_back(self, element):
        """Add element to end of array (like vector push_back)"""
        # If array is full, resize
        if self.size == self.capacity:
            # Create new array with double capacity
            new_capacity = self.capacity * 2
            new_arr = [0] * new_capacity

            # Copy elements (C-style copying)
            for i in range(self.size):
                new_arr[i] = self.arr[i]

            # Update array and capacity
            self.arr = new_arr
            self.capacity = new_capacity

        # Add new element at end
        self.arr[self.size] = element
        self.size += 1

    def pop_back(self):
        """Remove and return last element (like vector pop_back)"""
        if self.size == 0:
            raise IndexError("Vector is empty")

        # Get last element
        element = self.arr[self.size - 1]
        self.size -= 1

        # Shrink array if size is 1/4 of capacity
        if self.size > 0 and self.size == self.capacity // 4:
            new_capacity = self.capacity // 2
            new_arr = [0] * new_capacity

            # Copy elements (C-style copying)
            for i in range(self.size):
                new_arr[i] = self.arr[i]

            # Update array and capacity
            self.arr = new_arr
            self.capacity = new_capacity

        return element

    def at(self, index):
        """Get element at index (like vector at())"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.arr[index]

    def set(self, index, element):
        """Set element at index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.arr[index] = element

    def get_size(self):
        """Return current number of elements"""
        return self.size

    def get_capacity(self):
        """Return current capacity"""
        return self.capacity

    def is_empty(self):
        """Check if vector is empty"""
        return self.size == 0

    def __str__(self):
        """String representation showing actual elements"""
        return str([self.arr[i] for i in range(self.size)])

# Example usage
def main():
    # Create vector
    vec = DynamicArray()
    print(f"Initial vector: {vec}")
    print(f"Size: {vec.get_size()}, Capacity: {vec.get_capacity()}")

    # Add elements
    vec.push_back(10)
    vec.push_back(20)
    vec.push_back(30)
    print(f"\nAfter adding elements: {vec}")
    print(f"Size: {vec.get_size()}, Capacity: {vec.get_capacity()}")

    # Access elements
    print(f"\nElement at index 1: {vec.at(1)}")

    # Modify element
    vec.set(1, 25)
    print(f"After setting index 1 to 25: {vec}")

    # Remove elements
    popped = vec.pop_back()
    print(f"\nPopped element: {popped}")
    print(f"After pop_back: {vec}")
    print(f"Size: {vec.get_size()}, Capacity: {vec.get_capacity()}")

    # Test empty
    print(f"\nIs empty? {vec.is_empty()}")

if __name__ == "__main__":
    main()