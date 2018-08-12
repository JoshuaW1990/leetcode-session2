class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # use string at first
        s = str(x)
        return s[::-1]==s