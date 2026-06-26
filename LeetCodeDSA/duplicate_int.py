class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = list(set(nums))
        return len(nums) != len(nums2)