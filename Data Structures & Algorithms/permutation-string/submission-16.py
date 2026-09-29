class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            temp = s1
            for j in range(len(s1)):
                if s2[i + j] in temp:
                    temp = temp.replace(s2[i + j], "", 1)
                else:
                    break
            if temp == "":
                return True
        return False