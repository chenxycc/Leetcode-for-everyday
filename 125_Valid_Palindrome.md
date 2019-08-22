#### 双指针
```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and s[l].isalnum() is False:
                l += 1
            while l < r and s[r].isalnum() is False:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

```

#### 直接判断

```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_s = "".join(e.lower() for e in s if e.isalnum())
        return s_s == s_s[::-1]

```
