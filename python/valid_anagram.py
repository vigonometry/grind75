from collections import Counter

def valid_anagram(s: str, t: str) -> bool:
    sctr, tctr = dict(Counter(s)), dict(Counter(t))
    return sctr == tctr