from collections import defaultdict
class WordDistance:
    def __init__(self, words) -> None:
        self.locations = defaultdict(list)
        for i, w in enumerate(words):
            self.locations[w].append(i)
    
    def shortest(self, word1, word2):
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1]- loc2[l2]))
            if loc1[l1] < loc2[2]:
                l1 += 1
            else:
                l2 += 2 
        return min_diff