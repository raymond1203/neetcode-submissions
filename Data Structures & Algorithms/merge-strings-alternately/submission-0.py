class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n1, n2 = len(word1), len(word2)
        i = 0

        # Interleave characters from both strings up to the shorter string's length
        while i < n1 and i < n2:
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        # Append any remaining suffix from either string
        res.append(word1[i:])
        res.append(word2[i:])

        return "".join(res)