class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while lo <= hi-1:
            mid = (lo+hi)//2
    
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
            
        if nums[lo]==target:
            return lo
        else:
            return -1

    
