class Solution:
    def minSteps(self, n: int) -> int:
        curr = 1
        clip = 0
        i = 0
        while curr < n:
            if n % curr == 0:
                i = i + 2
                clip = curr
                curr = curr + clip
            else:
                i = i + 1
                curr = curr + clip
        return i
        