class Solution:
    def isValid(self, s: str) -> bool:
        # stack store the close brackets that converted from the open bracket
        # stack top is the bracket that need to be closed first

        # for loop s
            # if is open bracket convert to close
                # store into the stack
            # else (is close bracket)
                # if stack top the same pop
                # else return false
        # if stack is empty return True
        stack = []
        for bracket in s:
            if bracket == '(':
                stack.append(')')

            elif bracket == '{':
                stack.append('}')

            elif bracket == '[':
                stack.append(']')
            else:
                if not stack or stack.pop(-1) != bracket:
                    return False
    
        return True if not stack else False

        