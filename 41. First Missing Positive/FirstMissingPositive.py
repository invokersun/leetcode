class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L=len(nums)
        for m in range(L):
            if nums[m]>L:
                continue
            val = nums[m]-1
            while nums[m]>0 and val<L and nums[val] != nums[m]:
                nums[m],nums[val]=nums[val],nums[m]
                val = nums[m]-1
        for m in range(len(nums)):
            if nums[m] != m +1:
                return m +1
        return L+1
x = Solution()
print x.firstMissingPositive([3, 4, -1, 1])