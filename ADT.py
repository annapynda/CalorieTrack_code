import ctypes

class DynamicArray:
    """
    class represrnting Dynamic Array
    """

    def __init__(self):
        """Create an empty array."""
        self._size = 0
        self._capacity = 1
        self._A = (self._capacity * ctypes.py_object)()

    def __len__(self):
        """Return the size of array"""
        return self._size

    def __getitem__(self, k):
        """Return element at index k."""
        return self._A[k]

    def add(self, obj):
        """Add object to end of the array."""
        if self._size == self._capacity:
            self._changesize(2 * self._capacity)
        self._A[self._size] = obj
        self._size += 1

    def _changesize(self, c):
        """change size to capacity c."""
        B = (c * ctypes.py_object)()
        for k in range(self._size):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c



    def delete_item(self, item):
        """Delete first occurrence of item."""
        for k in range(self._size):
            if self._A[k] == item:
                for j in range(k, self._size - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._size - 1] = None
                self._size -= 1
                return None

        return "value not found"

    def __str__(self):
        """
        :return: the inside of array
        """
        a = ''
        for i in range(len(self)):
            a += str(self[i])  + ' '
        return a

