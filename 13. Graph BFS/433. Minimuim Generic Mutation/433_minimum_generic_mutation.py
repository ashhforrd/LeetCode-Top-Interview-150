class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        bank = set(bank)
        visited = set()

        if endGene not in bank:
            return -1

        geneString = ['A', 'T', 'G', 'C']

        while q:
            gene, numMutation = q.popleft()

            if gene == endGene:
                return numMutation

            for i in range(len(gene)):
                for g in geneString:
                    if gene[i] == g:
                        continue
                        
                    newGene = gene[:i] + g + gene[i + 1:]
                    
                    if newGene in bank and newGene not in visited:
                        visited.add(gene)
                        q.append([newGene, numMutation + 1])

        return -1