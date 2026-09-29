class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i, string in enumerate(strs):
            for char in string:
                encoded = encoded + 'l' + str(ord(char))
            encoded = encoded + 's'
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        decoded = []
        splittedS = s.split('s')[:-1]
        temp = ""
        for item in splittedS:
            splittedL = item.split('l')
            for n in splittedL:
                if n != '':
                    temp = temp + chr(int(n))
            decoded.append(temp)
            temp = ""

        return decoded