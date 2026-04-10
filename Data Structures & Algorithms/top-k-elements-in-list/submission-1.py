class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for i in range (0, len(nums)):
            curr_num = nums[i]

            # if num is in dict, then we add one to counter
            if curr_num in counter:
                count = counter.get(curr_num)
                counter[curr_num] = count + 1

            # if number isnt in dict, then the count is 1 now
            else:
                counter[curr_num] = 1
            

        # sort the dictionary by the value (count)
        sorted_counts = dict(sorted(counter.items(), key=lambda item: item[1]))

        # to get the k most frequent elements, we need to access the end of the list
        cond = False
        output = []
        cnt = 0
        while cond == False:
            for key in reversed(sorted_counts):
                output.append(key)
                cnt +=1
                if cnt == k:
                    cond = True
                    break
                else:
                    pass
                            
        return output


        
