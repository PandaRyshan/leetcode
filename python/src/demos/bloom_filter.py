import hashlib
from bitarray import bitarray


class BloomFilter:

    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_num):
            seed = str(i).encode('utf-8')
            digest = int(hashlib.md5(item.encode('utf-8') + seed).hexdigest(), 16)
            index = digest % self.size
            self.bit_array[index] = 1

    def exists(self, item):
        for i in range(self.hash_num):
            seed = str(i).encode('utf-8')
            digest = int(hashlib.md5(item.encode('utf-8') + seed).hexdigest(), 16)
            index = digest % self.size
            if not self.bit_array[index]:
                return False
        return True


bloom = BloomFilter(1000, 7)
bloom.add("hello")
print(bloom.exists("hello"))  # True
print(bloom.exists("world"))  # False
