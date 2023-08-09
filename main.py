class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        max = -1000000000

        if nums[len(nums) - 3] * nums[len(nums) - 2] * nums[len(nums) - 1] > max :
            max = nums[len(nums) - 3] * nums[len(nums) - 2] * nums[len(nums) - 1]
    
        if nums[0] * nums[1] * nums[len(nums) - 1] > max :
            max = nums[0] * nums[1] * nums[len(nums) - 1]

        return max