### 使用栈

```
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                else:
                    if l * r < 0 and l % r != 0:  # 考虑结果为负数的情况
                        stack.append(l // r + 1)
                    else:
                        stack.append(l // r)
        return stack.pop()
```
