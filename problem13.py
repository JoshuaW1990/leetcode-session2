class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return myDict[s]
        preCh = s[0]
        result = 0
        for i in range(1, len(s)):
            ch = s[i]
            if myDict[preCh] < myDict[ch]:
                result -= myDict[preCh]
            else:
                result += myDict[preCh]
            preCh = ch
        result += myDict[preCh]
        return result