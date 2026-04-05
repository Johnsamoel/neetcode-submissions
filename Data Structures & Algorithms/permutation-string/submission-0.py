class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counter = [0] * 26
        s2Counter = [0] * 26

        for i in range(len(s1)):
            s1Counter[(ord(s1[i]) - ord('a'))] += 1
            s2Counter[(ord(s2[i]) - ord('a'))] += 1
        
        matches = 0

        for idx in range(26):
            matches += (1 if s1Counter[idx] == s2Counter[idx] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            rIndex = (ord(s2[r]) - ord('a'))
            s2Counter[rIndex] +=1

            if s1Counter[rIndex] == s2Counter[rIndex]:
                matches += 1
            elif s1Counter[rIndex] +1 == s2Counter[rIndex]:
                matches -= 1

            lIndex = (ord(s2[l]) - ord('a'))
            s2Counter[lIndex] -=1
            if s1Counter[lIndex] == s2Counter[lIndex]:
                matches += 1
            elif s1Counter[lIndex]  - 1 == s2Counter[lIndex]:
                matches -= 1
            
            l += 1

        return matches == 26
