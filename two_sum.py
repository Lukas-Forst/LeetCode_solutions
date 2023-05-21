class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #to store the numbers in nums as keys and their corresponding indices as values
        num_indices = {}
        #We iterate through nums using enumerate() to access both the index and value of each number.
        for i, num in enumerate(nums):
            #For each number, we calculate the complement by subtracting it from the target.
            complement = target - num
            #If the complement is not found, we add the current number to num_indices with its index as the value.
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
