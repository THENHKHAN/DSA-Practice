# 1021. Remove Outermost Parentheses : https://leetcode.com/problems/remove-outermost-parentheses/

def removeOuterParentheses(S: str) -> str:
        res = []
        start = 0
        balance = 0
        for i in range(len(S)):
            if S[i] == "(":
                balance += 1
            elif S[i] == ")":
                balance -= 1
            if balance == 0:
                res.append(S[start+1:i]) # start+1 so that we can  leave last and the starting one
                print(i, "-> ", res)
                start = i+1# to move to the next

        return "".join(res)


s = "(()())(())"   #  ()()()
s = "(()())(())(()(()))"  #  ()()()()(())
s = "()()" # ['', '']==> "" since join so it will become ""
print(f"Current string of brackets : {s}")
print(f"After removing OuterMost Paranthesis : {removeOuterParentheses(s)}")

# Top 3 most upvotes: 
'''
https://leetcode.com/problems/remove-outermost-parentheses/discuss/270022/JavaC%2B%2BPython-Count-Opened-Parenthesis
https://leetcode.com/problems/remove-outermost-parentheses/discuss/270566/My-Java-3ms-Straight-Forward-Solution-or-Beats-100
https://leetcode.com/problems/remove-outermost-parentheses/discuss/2916928/One-Pass-or-FAANG-SDE-1-Interview

'''
'''
Complexity
Time complexity: O(n) //One pass
Space complexity: O(n) //For resultant string
'''