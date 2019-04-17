```
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        distance, stack, visited, lookup = 0, [beginWord], set([beginWord]), set(wordList)
        while stack:
            next_stack = []
            for word in stack:
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        trans_word = word[:i] + char + word[i+1:]
                        if trans_word not in visited and trans_word in lookup:
                            next_stack.append(trans_word)
                            visited.add(trans_word)
            distance += 1
            stack = next_stack
        return 0
```

> 不会做~_~
