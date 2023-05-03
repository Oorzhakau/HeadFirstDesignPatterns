class Node:
    def __init__(self, value, key=None, NextNode=None):
        self.key = key
        self.val = value
        self.next = NextNode


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def exists(self, key):
        curr = self.head.next
        while curr:
            if curr.key and curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def insert(self, key, value):
        result = self.exists(key)
        if result != -1:
            self.delete(key)
            new_node = Node(key=key, value=value, NextNode=self.head.next)
            self.head.next = new_node
            return
        self.head.next = Node(key=key, value=value, NextNode=self.head.next)

    def delete(self, key):
        if self.exists(key) != -1:
            prev = self.head
            curr = self.head.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                prev = curr
                curr = curr.next


class MyHashMap:
    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        self.bucketArray[bucket_index].insert(key, value)

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        return self.bucketArray[bucket_index].exists(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        self.bucketArray[bucket_index].delete(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(2, 5)
param_2 = obj.get(2)
print(param_2)
obj.put(2, 1)
param_2 = obj.get(2)
print(param_2)
param_3 = obj.get(3)
print(param_3)
param_2 = obj.get(2)
print(param_2)
obj.remove(2)
param_4 = obj.get(2)
print(param_4)
