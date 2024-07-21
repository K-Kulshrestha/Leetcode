from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)  # mapping the charCount to list of Anagrams

    for s in strs:
        count = [0] * 26  # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return list(res.values())

def main():
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "cba", "bac", "acb"],
        ["listen", "silent", "enlist", "inlets", "google", "gogole"],
    ]

    for i, test in enumerate(test_cases):
        print(f"Test Case {i+1}: {test}")
        result = groupAnagrams(test)
        print(f"Grouped Anagrams: {result}\n")

if __name__ == "__main__":
    main()
