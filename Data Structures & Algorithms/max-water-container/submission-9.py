class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        length = len(heights)-1
        curr_score = 0
        c = heights[a]
        d = heights [b]

        for i in range (0, len(heights)):
            c = heights[a]
            d = heights[b]

            score = (((b)-a) * min(c,d)) 
            #check if two pointers values is greater than current store
            if score > curr_score:
                curr_score = (((b)-a) * min(c,d))
                # move the lower value of a and b pointer inwards 1 index
                if min(c,d) == c:
                    #move a pointer in 1
                    a+=1
                    
                else:
                    b-=1
                
                continue


            else:
                # move the lower value of a and b pointer inwards 1 index
                if min(c,d) == c:
                    #move a pointer in 1
                    a+=1
                else:
                    b-=1
                
                continue

        return curr_score