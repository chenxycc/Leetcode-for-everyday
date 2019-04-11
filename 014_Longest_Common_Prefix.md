#### solution1:
```
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        sz, res = zip(*strs), ''
        for i in sz:
            if len(set(i))>1:
                break
            res += i[0]
        return res
```        
        
#### solution2:
```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return os.path.commonprefix(strs)#返回list中，所有path共有的最长的路径。
```
