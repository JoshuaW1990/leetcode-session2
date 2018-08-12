class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}
        for idx, num in enumerate(nums):
            if target - num in myDict:
                return [myDict[target-num], idx]
            else:
                myDict[num] = idx
        return None