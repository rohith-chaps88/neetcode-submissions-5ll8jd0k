class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(nums: List[int], target: int) -> int:
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

        
        for i in range(len(matrix)):
            if target >= matrix[i][0]:
                if target == matrix[i][0]:
                    return True
                else:
                    if target <= matrix[i][-1]:
                        if target == matrix[i][-1]:
                            return True
                        else:
                            output = binary_search(matrix[i], target)
                            if output == -1:
                                continue
                            else:
                                return True

        return False 
