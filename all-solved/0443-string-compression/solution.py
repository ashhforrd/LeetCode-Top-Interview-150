class Solution:
    def compress(self, chars: list[str]) -> int:
        char = ["", 0]
        write = 0
        for c in chars:
            if char[0] != "" and c != char[0]:
                chars[write] = char[0]
                write += 1
                if char[1] > 1:
                    s = str(char[1])
                    for k in s:
                        chars[write] = k
                        write += 1
                char = ["", 0]

            char = [c, char[1] + 1]
        
        if char:
            chars[write] = char[0]
            write += 1
            if char[1] > 1:
                s = str(char[1])
                for c in s:
                    chars[write] = c
                    write += 1
    
        return write
