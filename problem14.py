class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        commonStr = ""
        index = 0
        flag = True
        while flag:
            ch = ""
            for string in strs:
                if index == len(string):
                    flag = False
                    ch = ""
                    break
                elif ch != "" and ch != string[index]:
                    flag = False
                    ch = ""
                    break
                elif ch == "":
                    ch = string[index]
                else:
                    continue
            commonStr += ch
            index += 1
        return commonStr