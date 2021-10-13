def solution(N, coffee_times):
    import heapq

    class task:
        def __init__(self, idx, process):
            self.idx = idx
            self.process = process

        def __lt__(self, other):
            if self.process != other.process: return self.process < other.process
            return self.idx < other.idx

    # li = [4, 2, 2, 5, 3]

    nowTime = 0
    # n = 3

    heap = []
    for i in range(0, N):
        heap.append(task(i, coffee_times[i]))

    heapq.heapify(heap)

    result = []
    for i in range(N, len(coffee_times)):
        # 완료된 작업 빼기
        complete = heapq.heappop(heap)
        result.append(complete.idx + 1)
        nowtime = complete.process
        # 새로운작업 넣기 (끝나는 시간 기준)
        heapq.heappush(heap, task(i, coffee_times[i] + nowtime))

    while (heap):
        result.append(heapq.heappop(heap).idx + 1)


    return result


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
def solution(N, coffee_times):
    import heapq

    class task:
        def __init__(self, idx, process):
            self.idx = idx
            self.process = process

        def __lt__(self, other):
            if self.process != other.process: return self.process < other.process
            return self.idx < other.idx

    nowTime = 0

    heap = []
    for i in range(0, N):
        heap.append(task(i, coffee_times[i]))

    heapq.heapify(heap)

    result = []
    for i in range(N, len(coffee_times)):
        # 완료된 작업 빼기
        complete = heapq.heappop(heap)
        result.append(complete.idx + 1)
        nowtime = complete.process
        # 새로운작업 넣기 (끝나는 시간 기준)
        heapq.heappush(heap, task(i, coffee_times[i] + nowtime))

    while (heap):
        result.append(heapq.heappop(heap).idx + 1)

    return result