class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        MaxLength = 0
        window = set()
        n = len(s)

        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            length = (r-l)+1
            MaxLength = max(MaxLength,length)
        return(MaxLength)   