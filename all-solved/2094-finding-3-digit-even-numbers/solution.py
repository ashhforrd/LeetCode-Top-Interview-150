# class Solution:
#     def findEvenNumbers(self, digits: list[int]) -> list[int]:
#         result = []
#         def recursion(num, i, sets):
#             if len(num) == 3:
#                 if int(num) % 2 == 0:
#                     result.append(int(num))
#                 return
                        
#             for j in range(len(digits)):
#                 if j in sets:
#                     continue

#                 sets.add(j)
#                 recursion(num + str(digits[j]), j, sets)
#                 sets.remove(j)
        
#         for i in range(len(digits)):
#             if digits[i] == 0:
#                 continue

#             recursion(str(digits[i]), i, {i})

#         return sorted(set(result))

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        result = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if i == j:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    result.add(num)

        return sorted(result)
