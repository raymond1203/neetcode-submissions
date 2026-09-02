class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            # Find the '#' separating the length and the string content
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            
            res.append(s[start:end])
            i = end
            
        return res