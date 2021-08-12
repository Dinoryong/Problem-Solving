"""
[Topics]


[Sketch]


"""
from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.cnt = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)  # 초깃값 생성

    def insert(self, string):
        cur = self.head  # head부터 시작
        cur.cnt += 1  # count 1추가

        # 문자열 한 문자씩
        for s in string:
            # 자식에 해당 문자가 없다면
            if s not in cur.children:
                # 새로운 노드를 구성해서 넣어준다
                cur.children[s] = Node(s)
            # 다음 자식 문자로 현재 상태를 옮겨주고
            cur = cur.children[s]
            # 값을 1추가
            cur.cnt += 1

    def count(self, prefix):
        # head부터 시작
        cur = self.head

        # 접두사 문자열 문자 돌리기
        for s in prefix:
            # 자식에 문자가 없다면
            if s not in cur.children:
                # 0 return
                return 0
            # 현재 상태를 자식으로 옮겨준다
            cur = cur.children[s]

        # for문을 다 돌고나온 현재 상태의 cnt값을 return
        return cur.cnt


def make_trie(string, reverse):
    # 값이 없다면 0으로 초기화시키기 위해서 defaultdict사용
    trie_dic = defaultdict(Trie)

    # 문자열 돌리기
    for s in string:
        # 순서를 뒤집어야할 경우
        if reverse:
            s = s[::-1]

        # trie_dic의 처음 key는 문자열의 길이
        # 문자열의 길이를 하는 이유는 frodo, frodon이 있을때
        # fro??라는 query는 길이까지 계산해주어야하기 때문이다.
        trie_dic[len(s)].insert(s)

    return trie_dic


def count_word(trie, reverse_trie, query):
    # ? 제거
    new_query = query.replace('?', '')

    # ?로 시작된다면 역순으로 집어넣어준다
    # -> 역순으로 시작해야 처음부터 시작할때처럼 똑같은 조건으로 구해줄수있기 때문이다.
    # 처음 시작은 len(query) 문자열의 길이로 시작 이후 count함수를 통해 숫자 계산
    if query[0] == '?':
        return reverse_trie[len(query)].count(new_query[::-1])
    else:
        return trie[len(query)].count(new_query)


def solution(words, queries):
    answer = []

    trie = make_trie(words, False)
    reverse_trie = make_trie(words, True)
    for query in queries:
        temp = count_word(trie, reverse_trie, query)
        answer.append(temp)

    return answer
