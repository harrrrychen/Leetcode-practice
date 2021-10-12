class Solution:
    #1 my version
    def isValid(self, s: str) -> bool:
        #use Stack to implement
        stack_list = [0]
        
        for i in s:
            #incoming stage
            if i == ')' and stack_list[-1] =='(':
                stack_list.pop()
            elif i == ']' and stack_list[-1] =='[':
                stack_list.pop()
            elif i == '}' and stack_list[-1] =='{':
                stack_list.pop()
            else:
                stack_list.append(i)
            #check stage
            if len(stack_list) >= 2:
                if stack_list[-1] == ')' and stack_list[-2] =='(':
                    stack_list.pop()
                    stack_list.pop()
                elif stack_list[-1] == ']' and stack_list[-2] =='[':
                    stack_list.pop()
                    stack_list.pop()
                elif stack_list[-1] == '}' and stack_list[-2] =='{':
                    stack_list.pop()
                    stack_list.pop()
        if len(stack_list) > 1 : 
            return 0 
        else:
            return 1
    #2 use hashtable + put operation into if statement
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {"]": "[", "}": "{", ")": "("}
        for ch in s:
            if ch in ["[", "{", "("]:
                stack.append(ch)
            else:
                if not stack or stack.pop() != opening[ch]:
                    return False
        return not stack
