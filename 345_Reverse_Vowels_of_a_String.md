#### 双指针

```
class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        list_s = list(s)
        vowels = 'aeiou'
        while i <= j:
            if list_s[i].lower() not in vowels:
                i += 1
            elif list_s[j].lower() not in vowels:
                j -= 1
            else:
                list_s[i], list_s[j] = list_s[j], list_s[i]
                i += 1
                j -= 1
        return ''.join(list_s)
```
