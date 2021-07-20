"""
[Topics]
python - enumerate, dictionary(hash로 구현),

[Sketch]
쉬운 문제이나 최적화할 수 있는 여러 가지 방법이 숨어 있다.
"""
# sol 1. Brute Force : T.C = O(N^2)
# 첫번째 요소부터 마지막 요소까지 차례대로 모두 비교, 무차별 대입
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(i + 1, len(nums))):
                if nums[i] + nums[j] == target:
                    return [i, j]

# sol 2. in 으로 탐색 : 타겟에서 첫 번째 값을 뺀 target - n 이 존재하는지 탐색
# TC = O(N^2) 이지만, bruteforce 보다 훨씬 더 가볍고 빠르다. in 의 시간 복잡도는 O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

# sol 3. 비교,탐색 대신 첫 번째 수를 뺸 결과 키 조회
# T.C = O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        # 딕셔너리 조회는 평균적으로 T.C = O(1)
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺸 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

# sol. 4 조회 구조 개선 : 딕셔너리 저장과 조회를 for문 2개가 아닌 하나의 for 문으로 합쳐보기
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        # for 문 1개로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

# sol. 5 투 포인터 : 왼쪽 포인터와 오른쪽 포인터의 합이 타겟보다 크다면 오른쪽 포인터를 왼쪽으로
# 작다면 왼쪽 포인터를 오른쪽으로 옮기면서 값 조정
# 투 포인터를 쓰려면 nums 배열을 정렬 후에 써야 하나 , 그러면 인덱스값이 망가진다.
# 만약 구하려는 답이 인덱스 값이 아니라 그냥 값이었다면 투포인터가 적합
# 즉, 이 문제에서는 투 포인터르 풀이 불가
# 투포인터 T.C = O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 오름차순 정렬
        # nums.sort()
        left, right = 0, len(nums) - 1

        # 두 포인터가 완전 가운데로 모아져서 같아지거나 교차되기 전까지 반복
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right += 1
            else:
                return [left, right]

# sol 6. 고(Go) 구현








