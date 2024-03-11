# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 例如，121 是回文，而 123 不是。

def isPalindrome(x: int) -> bool:
        s = str(x)
        n = len(s)
        flag = True
        for i in range(n):
            if  s[i]!=s[n-1-i]:
                flag = False
                break
        return flag

x = 121
print('x is a palindrome?', isPalindrome(x))

