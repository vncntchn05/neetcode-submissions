class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        ans = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        seen = {s[l]}

        while l < r and r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.discard(s[l])
                    l += 1
                    if not l < r:
                        break
                l += 1
                r += 1
            else:
                seen.add(s[r])
                if r < len(s):
                    ans = max(ans, r - l + 1)
                r += 1
            
            print(l, r, ans)

        return ans