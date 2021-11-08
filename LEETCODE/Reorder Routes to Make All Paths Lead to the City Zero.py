'''


'''
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(graph, curNode, parent):
            n = 0
            for dest, direction in graph[curNode]:
                if dest != parent:
                    n += direction + dfs(graph, dest, curNode)
            return n

        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add((v, 1))
            graph[v].add((u, 0))

        return dfs(graph, 0, -1)


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        d = defaultdict(dict)
        for a, b in connections:
            d[a][b] = 1
            d[b][a] = 0

        seen = set()

        def dfs(a):
            seen.add(a)
            return sum(d[a][b] + dfs(b) for b in d[a] if b not in seen)

        return dfs(0)

'''
Okay, we
have
to
reorient
the
roads
for making our event successful.Let's go!

First
of
all, let
's think about the building graph and traversal.

Q & A:

Q: How
will
we
traverse
this
one?
A: Let
's build connections in opposite direction!

Q: What
the
traversal
will
give
us?
A: We
will
able
to
reach
out
to
all
nodes and count
nodes
that
we
added.

Stop.

Q: How
will
we
understand
that
node
has
been
added
by
us?
A: Let
's mark such nodes as "virtual" during building the graph.

Okay, so
we
just
need
to
make
a
DFS and compare if the
connection
between
the
current
node and prev is virtual?
Yes! Just
increment
your
counter, dude.

TC: O(V + E)
for DFS
    SC: O(V + E)
    for graph + O(E) for making opposite connections

'''
class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        if not connections: return 0

        graph = collections.defaultdict(dict)

        for fr, to in connections:
            graph[fr][to] = 'existing'
            graph[to][fr] = 'virtual'

        visited = [False] * n

        self.result = 0

        self.dfs(graph, 0, -1, visited)

        return self.result

    def dfs(self, graph, vertex, prev, visited):
        visited[vertex] = True

        if graph[vertex].get(prev, 'N/A') == 'virtual':
            self.result += 1

        for nei, type in graph[vertex].items():
            if not visited[nei]:
                self.dfs(graph, nei, vertex, visited)

''''''


class Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    adj_out = collections.defaultdict(list)
    adj_in = collections.defaultdict(list)

    for st, fin in connections:
      adj_out[st] += [fin]
      adj_in[fin] += [st]

    S = [0] + adj_out[0] + adj_in[0]
    changed = len(adj_out[0])
    visited = set(S)

    while S:
      node = S.pop()

      for outn in adj_out[node]:
        if outn not in visited:
          visited.add(outn)
          changed += 1
          S.append(outn)

      for inn in adj_in[node]:
        if inn not in visited:
          visited.add(inn)
          S.append(inn)

    return changed
