class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count_ = 0
        count_m = 0
        while i != len(nums):
            if nums[i] == 1:
                count_ += 1
                if count_ >= count_m:
                    count_m = count_
                i+=1
            else:
                count_ = 0
                i+=1
        return count_m
