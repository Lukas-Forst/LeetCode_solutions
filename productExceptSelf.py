class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = nums.count(0)
        if 0 not in nums:
            total = 1
            for num in nums:
                total *= num
            ret = [total // num for num in nums]
            return ret
        elif count_zero == 1:
            total = 1
            ret = []
            #calculate total
            for i in nums:
                if i == 0:
                    total*=1
                else:
                    total*=i
            for i in nums:
                if i != 0:
                   ret.append(0)
                else:
                    ret.append(total)
            return ret
        else:
            return [0 for i in nums]            
