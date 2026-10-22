class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(heap)

        prev = None
        ans = ""
        while heap or prev:
            if not heap and prev:
                return ""

            cnt, char = heapq.heappop(heap)
            ans += char
            cnt += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt < 0:
                prev = [cnt, char]

        return ans
            
        
