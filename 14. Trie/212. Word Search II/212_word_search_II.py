class WordDictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        curr = self.dictionary

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr["*"] = True

    def search(self, word: str) -> bool:
        curr = self.dictionary

        def dfs(current, i):
            if i == len(word):
                return "*" in current

            if word[i] == ".":
                for c in current:
                    if c != "*" and dfs(current[c], i + 1):
                        return True
                return False
            else:
                if word[i] in current:
                    return dfs(current[word[i]], i + 1)
                else:
                    return False
        
        return dfs(curr, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)