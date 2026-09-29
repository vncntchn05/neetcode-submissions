class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPos = sorted(zip(position, speed), key=lambda x: (-x[0], -x[1]))
        fleets = set()
        fastest = float('-inf')

        for p, s in sortedPos:
            t = ((target - p) / s)
            if fastest < t:
                fleets.add(t)
            fastest = max(fastest, t)

        return len(fleets)