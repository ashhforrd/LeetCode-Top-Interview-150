class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        studentsMap, sandwichesMap = {}, {}

        for s in students:
            studentsMap[s] = studentsMap.get(s, 0) + 1

        for s in sandwiches:
            sandwichesMap[s] = sandwichesMap.get(s, 0) + 1
        
        q = deque(students)

        while q and sandwiches:

            if sandwiches[0] not in studentsMap or studentsMap[sandwiches[0]] == 0:
                return len(q)

            shape = q.popleft()
            
            if shape == sandwiches[0]:
                s = sandwiches.pop(0)
                studentsMap[shape] -= 1 
                sandwichesMap[s] -= 1
            else:
                q.append(shape)

        return 0
