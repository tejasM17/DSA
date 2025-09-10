class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(l) for l in languages]
        need = set()
        for u, v in friendships:
            if langs[u - 1].intersection(langs[v - 1]):
                continue
            need.add(u - 1)
            need.add(v - 1)
        res = float('inf')
        for l in range(1, n + 1):
            cnt = 0
            for u in need:
                if l not in langs[u]:
                    cnt += 1
            res = min(res, cnt)
        return 0 if res == float('inf') else res
