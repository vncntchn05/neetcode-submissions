class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        maxf = 0
        maxes = 1

        for task in tasks:
            freq[task] += 1
            if freq[task] > maxf:
                maxf = freq[task]
                maxes = 1
            elif freq[task] == maxf:
                maxes += 1
            
        return max(maxf + (maxf - 1) * n + maxes - 1, len(tasks))
        