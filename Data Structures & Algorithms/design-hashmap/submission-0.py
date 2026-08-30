class ListNode:
    def __init__(self, key: int = -1, value: int = -1, next: 'ListNode' = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:
    def __init__(self):
        # A prime number of buckets helps distribute keys evenly
        self.size = 1009
        self.buckets = [ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        
        # Traverse to check if key already exists
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value  # Update existing value
                return
            curr = curr.next
        
        # Insert new node at the end of the chain
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        curr = self.buckets[index].next
        
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
            
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # Unlink the node
                return
            curr = curr.next