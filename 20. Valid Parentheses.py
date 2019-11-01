class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' or i == ']' or i == '}':
                if stack:
                    match = stack.pop()
                    if i != dictionary[match]:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
