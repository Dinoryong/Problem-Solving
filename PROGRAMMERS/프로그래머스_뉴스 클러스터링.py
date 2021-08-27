"""
[topics]
python set : 집합 자료, 중복을 허용하지 않는다->자료형의 중복 제거하기 위한 필터 역할 가능, 인덱싱 불가능
, 순서가 없다
set 교집합 : & 쓰거나 intersection
set 합집합 : | 쓰거나 union
python count() : 변수.count(찾는 요소)
문자열 안에서 찾고 싶은 문자의 개수를 찾을 때
때"""
#
def solution(str1, str2):

    # 교집합 원소의 개수
    def intersection_set(A, B):
        n = 0
        for x in set(A):
            if x in B:
                n += min(A.count(x), B.count(x))
        return n

    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    A, B = [], []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            A.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            B.append(str2[i] + str2[i + 1])

    # Edge case A,B 모두가 공집합인 경우에 자카드 유사도는 1
    if (not A) and (not B):
        return 65536

    # 교집합의 원소의 개수 구하기
    n = intersection_set(A, B) if len(A) < len(B) else intersection_set(B,A)

    answer = n / (len(A) + len(B) - n)

    return int(answer * 65536)

# 다른 사람
def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536
