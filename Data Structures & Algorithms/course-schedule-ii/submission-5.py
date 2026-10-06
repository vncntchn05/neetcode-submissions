class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        degrees = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for u, v in prerequisites:
            degrees[v] += 1
            adj[u].append(v)

        q = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                q.append(i)

        while q:
            c = q.popleft()
            if c not in ans:
                ans.append(c)

            for n in adj[c]:
                degrees[n] -= 1
                if degrees[n] == 0:
                    q.append(n)
        ans.reverse()
        return ans if len(ans) == numCourses else []