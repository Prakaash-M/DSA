#pick a string as reference with min length
#loop through based on the length of the min length string
#compare the first character of all the strings
#if all the character matches then add it to the longest string or return the value of longest string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            for j in strs:
                if j[i] != char:
                    return shortest_str[:i]
        return shortest_str            

            




