from collections import deque

from .helper import clamp

__all__ = [
    'Jaro',
    'JaroWinkler'
]


class Jaro:
    def similarity(self, a: str, b: str) -> float:
        """
        Calculate the Jaro similarity between two strings
        :param a: string a
        :type a: str
        :param b: string b
        :type b: str
        :return: the similarity score where 1 is the same and 0 is completely different
        :rtype: float
        """
        if a == b:
            return 1

        lenA, lenB = len(a), len(b)

        matchBound = max(lenA, lenB) // 2 - 1

        matches = 0

        matchingA = [False for _ in range(lenA)]
        matchingB = [False for _ in range(lenB)]

        for i, ai in enumerate(a):
            for j in range(max(i - matchBound, 0), min(i + matchBound + 1, lenB)):
                if ai == b[j]:
                    matches += 1
                    matchingA[i] = True
                    matchingB[j] = True

                    break

        if matches == 0:
            return 0

        matchesA = deque()
        matchesB = deque()

        for i, m in enumerate(matchingA):
            if m:
                matchesA.append(a[i])

        for i, m in enumerate(matchingB):
            if m:
                matchesB.append(b[i])

        transpositions = 0

        while matchesA:
            char = matchesA.popleft()

            if matchesB[0] == char:
                matchesB.popleft()
            else:
                matchesB.remove(char)
                transpositions += 1

        return (matches / lenA + matches / lenB + (matches - transpositions) / matches) / 3


class JaroWinkler(Jaro):
    def __init__(self, *, maxLength: int = 4, p: float = 0.1) -> None:
        """
        :param maxLength: the maximum length of the prefix term
        :type maxLength: int
        :param p: the prefix scaling factor
        :type p: float
        """
        self.maxLength = maxLength
        self.p = clamp(p, 0, 1 / maxLength)

    def similarity(self, a: str, b: str) -> float:
        """
        Calculate the Jaro-Winkler similarity between two strings
        :param a: string a
        :type a: str
        :param b: string b
        :type b: str
        :return: the similarity score where 1 is the same and 0 is completely different
        :rtype: float
        """
        jaro = super(JaroWinkler, self).similarity(a, b)

        prefix = 0
        while a[prefix] == b[prefix] and prefix < self.maxLength:
            prefix += 1

        return jaro + self.p * prefix * (1 - jaro)
