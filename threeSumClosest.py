from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            raise ValueError("Input must have at least three numbers.")
        
        nums.sort()
        # Initialize closest_sum to sum of first three (valid since n >= 3)
        closest_sum = nums[0] + nums[1] + nums[2]
        best_diff = abs(closest_sum - target)
        
        for i in range(n - 2):
            # Two pointers for the subarray nums[i+1..n-1]
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                diff = curr - target
                
                # If exact match, return immediately
                if diff == 0:
                    return target
                
                # Update closest if this is better
                if abs(diff) < best_diff:
                    best_diff = abs(diff)
                    closest_sum = curr
                
                # Move pointers
                if diff > 0:
                    # current sum too large -> decrease by moving right leftwards
                    right -= 1
                else:
                    # current sum too small -> increase by moving left rightwards
                    left += 1
        
        return closest_sum
