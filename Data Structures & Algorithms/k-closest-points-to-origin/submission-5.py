class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = sorted(points, key=lambda point: math.sqrt(point[0] ** 2 + point[1] ** 2))
        
        return arr[0:k]