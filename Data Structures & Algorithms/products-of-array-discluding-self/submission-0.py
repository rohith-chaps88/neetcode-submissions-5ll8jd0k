class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        product = 1
        length = len(nums)
        for i in range(length):

            for j in range(0,i):
                product = product * nums[j]

            for k in range(i+1, length):
                product = product * nums[k]

            output.append(product)
            product = 1


        return output

