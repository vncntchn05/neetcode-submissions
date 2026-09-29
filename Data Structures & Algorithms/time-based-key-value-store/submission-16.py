class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, h = 0, len(self.timemap[key]) - 1

        if not self.timemap[key] or self.timemap[key][0][1] > timestamp:
            return ""

        m = 0
        while l <= h:
            m = (l + h) // 2
            if self.timemap[key][m][1] == timestamp:
                return self.timemap[key][m][0]
            elif self.timemap[key][m][1] > timestamp:
                h = m - 1
                m = m - 1
            else:
                l = m + 1

        return self.timemap[key][m][0]