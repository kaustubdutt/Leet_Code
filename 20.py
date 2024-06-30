class Solution:
    def isValid(self, s: str) -> bool:
        close_elements = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in close_elements:
                if stack != []:
                    top_element = stack.pop()
                else:
                    return False
                if close_elements[char] != top_element:
                    return False
            else:
                stack.append(char)
        if stack == []:
            return True
        else:
            return False