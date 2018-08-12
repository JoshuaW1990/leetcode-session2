class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # double pointer + set
        record = set()
        head, tail = 0, 0
        maxLength = 0
        while head < len(s):
            if s[head] not in record:
                record.add(s[head])
            else:
                while s[tail] != s[head]:
                    record.remove(s[tail])
                    tail += 1
                tail += 1
            head += 1
            maxLength = max(maxLength, len(record))
        return maxLength

