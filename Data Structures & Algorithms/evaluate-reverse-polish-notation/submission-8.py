class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # for loop token
            # if operator: stack pop top 2 to calculate
            # if num: stack store numbers
  
        stack = []
        for t in tokens:
            operator = ['+', '-', '*','/']
            if t in operator:
                top = stack.pop(-1)
                second = stack.pop(-1)
                if t == '+':
                    stack.append(second + top)

                elif t == '-':
                    stack.append(second - top)

                elif t == '*':
                    stack.append(second * top)
                
                elif t == '/':
                    stack.append(int(second / top))
            else:
                stack.append(int(t))
        
        return stack.pop(-1)


            
        