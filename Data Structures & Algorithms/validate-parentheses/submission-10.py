from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

      
        # create a hashmap so we can make key value pairs of the types of brackets
        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = deque()
        if len(s) <= 1:
            return False

        for i in s:
            if not close_to_open.get(i):
                stack.append(i)

            else:
                if len(stack) > 0:
                    top_of_stack = stack.pop()
                    if close_to_open.get(i) == top_of_stack:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) !=0 and not close_to_open.get(stack.pop()):
            return False
        return True

