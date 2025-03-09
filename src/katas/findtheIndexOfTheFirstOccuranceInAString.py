class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #easy way - 
        #return haystack.find(needle)
        #two pointers
        i,j = 0, 0
        while i < len(haystack) and j < len(needle):
            start = i
            while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return start
            i = start + 1
            j = 0
        return -1