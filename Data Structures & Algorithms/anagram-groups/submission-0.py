class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue

            curr_list = [strs[i]]
            used[i] = True

            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    curr_list.append(strs[j])
                    used[j] = True

            output.append(curr_list)

        return output
