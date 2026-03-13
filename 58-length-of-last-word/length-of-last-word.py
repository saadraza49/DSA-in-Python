class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) - 1
        count = 0
        while l >= 0 and s[l] == " ":
            l -= 1
        while l >= 0 and s[l] != " ":
            count += 1
            l -= 1
        return count