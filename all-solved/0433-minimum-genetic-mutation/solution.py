class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        q = deque([(startGene, 0)])
        visited = set()

        if endGene not in bank:
            return -1

        genes = ['A', 'T', 'G', 'C']
        
        while q:
            gene, mutations = q.popleft()

            if gene == endGene:
                return mutations

            for i in range(len(gene)):
                for g in genes:
                    if gene[i] == g:
                        continue
                    
                    gen = gene[:i] + g + gene[i + 1:]

                    if gen in bank and gen not in visited:
                        visited.add(gen)
                        q.append([gen, mutations + 1])

        return -1
