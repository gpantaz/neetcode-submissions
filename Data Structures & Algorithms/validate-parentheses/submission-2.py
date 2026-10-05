class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closing_brackets = ")]}"
        def is_matching(bracket1, bracket2):
            return bracket1+bracket2 in ("()", "[]", "{}")
        
        s = [chara for chara in s]
        while s:
            current_chara = s.pop(0)
            if not stack:
                if current_chara in closing_brackets:
                    return False
                stack.append(current_chara)
            
            elif current_chara not in closing_brackets:
                stack.append(current_chara)

            elif is_matching(stack[-1], current_chara):
                stack.pop(-1)

            else:
                return False
        
        return len(stack) == 0
            
