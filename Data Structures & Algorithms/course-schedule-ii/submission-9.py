class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        degrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            degrees[v] += 1

        q = deque()
        for i in range(numCourses):
            if degrees[i] == 0:
                q.append(i)

        while q:
            c = q.popleft()
            if c not in ans:
                ans.append(c)
                
            for nei in adj[c]:
                degrees[nei] -= 1
                if degrees[nei] == 0:
                    q.append(nei)
        return ans[::-1] if len(ans) == numCourses else []

        
        