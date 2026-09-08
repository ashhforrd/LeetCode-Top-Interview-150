class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        q = deque([(beginWord, 1)])
        wordSet = set(wordList)
        wordLength = len(beginWord)

        while q:
            word, l = q.popleft()

            if word == endWord:
                return l
            
            for i in range(wordLength):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append([newWord, l + 1])

        return 0