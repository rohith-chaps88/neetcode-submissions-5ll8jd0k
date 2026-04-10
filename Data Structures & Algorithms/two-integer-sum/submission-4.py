class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # time complexity needs to be O(n) so we cant loop through each element and check every pari of numbers

       # to ensure O(n) we can use HashMaps. 
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i