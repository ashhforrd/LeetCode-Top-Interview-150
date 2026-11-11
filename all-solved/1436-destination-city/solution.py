class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        start = set()

        for a, _ in paths:
            start.add(a)

        for _, b in paths:
            if b not in start:
                return b
