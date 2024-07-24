from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    # Using a set to store unique elements
    if len(set(nums)) == len(nums):
        return False
    return True

# Example usage
def main():
    test_cases = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([1, 1, 1, 1], True),
        ([3, 1, 4, 2], False),
        ([], False)
    ]

    for nums, expected in test_cases:
        result = containsDuplicate(nums)
        print(f"containsDuplicate({nums}) = {result} (expected: {expected})")

if __name__ == "__main__":
    main()
