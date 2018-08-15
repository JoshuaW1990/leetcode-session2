class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                tmp = stack.pop()
                if (ch == ")" and tmp in "{[") or (ch == "}" and tmp in "([") or (ch == "]" and tmp in "({"):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False