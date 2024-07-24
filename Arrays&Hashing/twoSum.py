from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

# Example usage
def main():
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4], 7, [2, 3]),
        ([1, 5, 1, 5], 6, [0, 1])
    ]

    for nums, target, expected in test_cases:
        result = twoSum(nums, target)
        print(f"twoSum({nums}, {target}) = {result} (expected: {expected})")

if __name__ == "__main__":
    main()
