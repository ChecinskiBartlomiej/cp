#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        j = 0
        m = len(numbers) - 1

        while j < m:
            sum = numbers[j] + numbers[m]
            if sum < target:
                j += 1
            elif sum > target:
                m -= 1
            else:
                return([j+1, m+1])
                