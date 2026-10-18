class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegs = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
            indegs[u] += 1

        q = deque()
        ans = []

        for i in range(numCourses):
            if indegs[i] == 0:
                q.append(i)
        
        while q:
            c = q.popleft()
            ans.append(c)
        
            for nei in adj[c]:
                indegs[nei] -= 1
                if indegs[nei] == 0:
                    q.append(nei)

        return ans if len(ans) == numCourses else []