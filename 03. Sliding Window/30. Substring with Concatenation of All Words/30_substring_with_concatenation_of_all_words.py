class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = []
        strLen, wordLen = len(s), len(words[0])

        wordMap = {}
        for word in words:
            wordMap[word] = wordMap.get(word, 0) + 1
        
        for i in range(wordLen):
            left, right = i, i
            wordHash = wordMap.copy()

            while right + wordLen <= strLen:
                word = s[right: right + wordLen]
                right += wordLen

                if word in wordHash:
                    wordHash[word] -= 1

                    while wordHash[word] < 0:
                        leftWord = s[left: left + wordLen]
                        wordHash[leftWord] += 1
                        left += wordLen
                    
                    if all(v == 0 for v in wordHash.values()):
                        indices.append(left)
                        leftWord = s[left: left + wordLen]
                        wordHash[leftWord] += 1
                        left += wordLen

                else:
                    wordHash = wordMap.copy()
                    left = right
                
        return indices