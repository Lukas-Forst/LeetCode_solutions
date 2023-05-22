class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Initialize a variable to keep track of the maximum wealth
        max_ = 0
        # Iterate through each customer's accounts
        for i in range(len(accounts)):
            # Calculate the wealth for the current customer by summing their accounts
            curr = sum(accounts[i])

            # Check if the current wealth is greater than the current maximum wealth
            if curr > max_:
                # If so, update the maximum wealth
                max_ = curr

        # Return the maximum wealth
        return max_
