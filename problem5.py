class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        start, end = 0, 0
        for i in xrange(len(s)):
            len1 = self._expandString(s, i, i)
            len2 = self._expandString(s, i, i+1)
            maxLen = max(len1, len2)
            if  maxLen > end - start:
                start = i - (maxLen - 1) / 2
                end = i + maxLen / 2
        return s[start: end+1]
        


    def _expandString(self, string, left, right):
        l, r = left, right
        while l >= 0 and r < len(string) and string[l]==string[r]:
            l -= 1
            r += 1
        return r - l - 1

                        
