# Problem-Solving

------------

> [toc]



## Today I learned :books:



![img](README.assets/68747470733a2f2f63646e2e6472696262626c652e636f6d2f75736572732f313834383833382f73637265656e73686f74732f343233363431302f6c616d705f616e696d6174696f6e2e676966)



## 알고리즘 분류

알고리즘 분류는 다음 표를 기본으로 합니다.

| 태그명       | 의미                 |
| ------------ | -------------------- |
| backtracking | 백트래킹             |
| bfs          | 너비우선탐색         |
| big          | 매우큰수             |
| binary       | 이분탐색             |
| brute        | 부르트포스(전부대입) |
| combi        | 조합                 |
| dfs          | 깊이우선탐색         |
| divide       | 분할정복기법         |
| dynamic      | 동적계획법           |
| graph        | 그래프               |
| greedy       | 탐욕알고리즘         |
| map          | key,value구조        |
| number       | 정수론(소수...)      |
| queue        | 큐                   |
| recursive    | 재귀                 |
| simulation   | 시뮬레이션           |
| sort         | 정렬                 |
| stack        | 스택                 |
| string       | 문자열               |
| tree         | 트리구조             |



## 🗂 폴더 구조

폴더명에 문제 번호와 문제 종류 태그로 구성 되어있습니다

```
number_tags
├── README.md   # 문제 풀이 정리 기록
├── answer.cpp  # 문제 풀이 파일 (.cpp, .js, .py ...)
└── data        # input & output 정리
    ├── data.txt    # test cases (input & output)
    └── input.txt   # input
```

------

## 🏷 문제 태그

다음 표에 나와있는 태그 외에도 다양한 태그들이 존재합니다.

<details open="" style="box-sizing: border-box; display: block; margin-bottom: 16px; margin-top: 0px;"><summary style="box-sizing: border-box; display: list-item; cursor: pointer;">문제 태그 표 확인하기</summary><table style="box-sizing: border-box; border-collapse: collapse; border-spacing: 0px; margin-bottom: 16px; margin-top: 0px; display: block; max-width: 100%; overflow: auto; width: max-content;"><thead style="box-sizing: border-box;"><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><th align="center" style="box-sizing: border-box; padding: 6px 13px; font-weight: 600; border: 1px solid var(--color-markdown-table-border);">태그명</th><th align="center" style="box-sizing: border-box; padding: 6px 13px; font-weight: 600; border: 1px solid var(--color-markdown-table-border);">의미</th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">backtracking</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">백트래킹</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">bfs</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">너비 우선 탐색</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">big</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">매우 큰 수</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">brute</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">부르트 포스 (전부 대입)</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">combination</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">조합</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">dfs</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">깊이 우선 탐색</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">divide</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">분할 정복 기법</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">dynamic</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">동적계획법</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">extreme</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">최대 최소 값 찾기</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">find</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">검색</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">graph</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">그래프</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">greedy</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">탐욕 알고리즘</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">iteration</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">반복문</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">list</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">큐, 스택, 리스트</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">mod</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">나머지</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">notation</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">진법 문제</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">number</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">정수론 (소수...)</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">recursive</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">재귀</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">sequence</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">순열</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">simulation</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">시뮬레이션</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">sort</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">정렬</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">string</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">문자열</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">table</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">key, value 구조</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-tertiary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">tree</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">트리 구조</td></tr><tr style="box-sizing: border-box; background-color: var(--color-bg-primary); border-top: 1px solid var(--color-markdown-table-tr-border);"><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">unique</td><td align="center" style="box-sizing: border-box; padding: 6px 13px; border: 1px solid var(--color-markdown-table-border);">유일한 값들의 집합</td></tr></tbody></table></details>

-----



## About

The repository of problem solving (especially algorithm problems of computer science)

### Topics

[algorithm](https://github.com/topics/algorithm) [problem-solving](https://github.com/topics/problem-solving)

## 언어

Python 을 기본으로 작성되었고, 일부 문제는 JAVA 및 JAVASCRIPT로 작성되었습니다.



