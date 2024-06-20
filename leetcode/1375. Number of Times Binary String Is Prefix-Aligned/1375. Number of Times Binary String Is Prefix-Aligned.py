class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        curr = 0
        cnt = 0
        for f in flips:
            curr ^= 1 << f - 1
            l = curr.bit_length()
            # print(l,bin(curr),(1<<l)-1)
            cnt += curr == (1 << l) - 1
        return cnt 
