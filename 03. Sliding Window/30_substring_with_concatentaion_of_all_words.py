class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        output = []
        lenS = len(s)
        lenW = len(words[0])

        baseMap = {}
        for w in words:
            baseMap[w] = baseMap.get(w, 0) + 1

        for offset in range(lenW):
            L = offset
            R = offset
            hashWords = baseMap.copy()

            while R + lenW <= lenS:
                word = s[R:R+lenW]
                R += lenW

                if word in hashWords:
                    hashWords[word] -= 1

                    while hashWords[word] < 0:
                        leftWord = s[L:L+lenW]
                        hashWords[leftWord] += 1
                        L += lenW
                    
                    if all(v == 0 for v in hashWords.values()):
                        output.append(L)
                        firstWord = s[L:L+lenW]
                        hashWords[firstWord] += 1
                        L += lenW
                else:
                    hashWords = baseMap.copy()
                    L = R
            
        return output