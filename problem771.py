class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        myDict = {}
        for ch in S:
            if ch not in myDict:
                myDict[ch] = 1
            else:
                myDict[ch] += 1
        cnt = 0
        for ch in J:
            cnt += myDict.get(ch, 0)
        return cnt