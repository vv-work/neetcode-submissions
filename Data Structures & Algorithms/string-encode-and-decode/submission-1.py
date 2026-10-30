class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            tmp =f'{len(s)}#{s}'
            res.append(tmp)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0 
        while i<len(s):
            l=0 
            while s[i]!="#":
                l=l*10 + int(s[i])
                i+=1
            i+=1
            res.append(s[i:i+l])
            i=i+l

        return res