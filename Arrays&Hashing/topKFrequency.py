from typing import List

def topKFrequency(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

def main():
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 4, 4, 4, 5, 5, 5, 6, 6, 7], 3, [4, 5, 6]),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2, [4, 3]),
        ([1, 1, 2, 2, 3, 3], 3, [1, 2, 3])
    ]

    for nums, k, expected in test_cases:
        result = topKFrequency(nums, k)
        print(f"topKFrequency({nums}, {k}) = {result} (expected: {expected})")

if __name__ == "__main__":
    main()
