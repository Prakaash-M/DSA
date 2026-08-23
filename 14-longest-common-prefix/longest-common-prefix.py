# 1. Find the shortest string to use as our bounds
# 2. Iterate using enumerate to keep track of the index (i) and character (char)
# 3. Compare with every string
# 4. Return a slice of the string
# 5. If we finish the loop, the entire shortest string is the prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            for j in strs:
                if j[i] != char:
                    return shortest_str[:i]
        return shortest_str            

            




