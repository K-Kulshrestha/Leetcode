from typing import List

def productOfArrayExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    # Calculate prefix products
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    # Calculate postfix products
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

# Example usage
def main():
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 1, 2, 3], [6, 0, 0, 0]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([2, 0, 1, 4], [0, 8, 0, 0])
    ]

    for nums, expected in test_cases:
        result = productOfArrayExceptSelf(nums)
        print(f"productOfArrayExceptSelf({nums}) = {result} (expected: {expected})")

if __name__ == "__main__":
    main()
