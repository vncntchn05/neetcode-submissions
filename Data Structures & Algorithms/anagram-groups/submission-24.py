class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        words = []

        for string in strs:
            if len(words) == 0:
                words.append(string)
                ans.append([string])
                continue
                
            for i, word in enumerate(words):
                p = True
                temp = word

                if len(temp) != len(string):
                    p = False
                    continue

                for char in string:
                    temp = temp.replace(char, '', 1)

                if temp != '':
                    p = False
                    continue
                else:
                    ans[i].append(string)
                    break

            if not p:
                words.append(string)
                ans.append([string])

        return ans

