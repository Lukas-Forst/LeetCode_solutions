class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[0+writer], nums[i] = nums[i], nums[0+writer]
                writer+=1
        return writer
