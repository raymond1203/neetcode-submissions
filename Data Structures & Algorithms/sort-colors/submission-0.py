class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0           # Boundary for 0s
        mid = 0           # Current element being evaluated
        high = len(nums) - 1  # Boundary for 2s

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Note: mid is not incremented here because the swapped 
                # element from nums[high] has not been processed yet.