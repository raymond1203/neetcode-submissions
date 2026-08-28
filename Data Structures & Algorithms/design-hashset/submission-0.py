class MyHashSet:

    def __init__(self):
        # A prime number of buckets to reduce collisions
        self.num_buckets = 1009
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        return key in bucket