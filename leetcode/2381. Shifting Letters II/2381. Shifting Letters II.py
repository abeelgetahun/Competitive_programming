class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
            difference = [0] * len(s)
            for start, end, direction in shifts:
                difference[start] += 1 if direction == 1 else -1
                if end + 1 < len(s):
                    difference[end + 1] -= 1 if direction == 1 else -1
            print(difference)
            res = ""
            shift_value = 0
            for i in range(len(s)):
                shift_value += difference[i]
                res += chr((ord(s[i]) - 97 + shift_value) % 26 + 97)

            return res
