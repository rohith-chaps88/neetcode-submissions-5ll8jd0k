class Solution:

  
    def encode(self, strs: List[str]) -> str:
        global_store = []
        msg = ""

        for word in strs:
            msg += str(len(word))
            msg += str(":")
            for char in word:
                msg += str(char)
            

        return msg
    
    def decode(self, s: str) -> List[str]:
        output = []
        word = ""
        num = ""
        idx = 0

        while idx < len(s):

            curr_char = s[idx]

            if curr_char != ":":
                num += curr_char
                idx += 1

            else:
                idx += 1
                num = int(num)
                
                for _ in range(num):
                    word += str(s[idx])
                    idx +=1

                output.append(word)
                word = ""
                num = ""
                
        return output             


               



        return output

            

