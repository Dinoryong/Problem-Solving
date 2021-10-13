class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0

        for num in nums:
            num = str(num)
            result = len(num)
            if (result % 2) == 0:
                answer += 1

        return answer