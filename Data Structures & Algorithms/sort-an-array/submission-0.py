class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(length: int, i: int) -> None:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < length and nums[left] > nums[largest]:
                largest = left

            if right < length and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(length, largest)

        # Step 1: Build max-heap (bottom-up)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Step 2: Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # Move current max to the end
            heapify(i, 0)                         # Restore heap property on the reduced heap

        return nums