# sol 1. 정렬
def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
    return 0

# sol 2. range 에서 max() 써서
def solution(citations):
    for i in range(max(citations), -1, -1):
        if sum(1 for j in citations if j >= i) >= i:
            break
    return i

# sol 3. 역정렬
def solution(citations):
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        if n <= i:
            return i
    return len(citations)