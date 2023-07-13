def isAnagram(self, s: str, t: str) -> bool:
        scount = {}
        tcount = {}
        for c in s:
            scount[c] = 1 + scount.get(c, 0)
        for c in t:
            tcount[c] = 1 + tcount.get(c, 0)
        return scount == tcount
