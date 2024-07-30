from typing import List

def longestConsecutiveSequence(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if it's the start of the sequence
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

def main():
    # Test cases
    test_cases = [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
        [],
        [1, 2, 0, 1],
    ]

    # Execute the function with each test case and print the result
    for i, nums in enumerate(test_cases):
        result = longestConsecutiveSequence(nums)
        print(f"Test case {i+1}: {nums}")
        print(f"Longest consecutive sequence length: {result}\n")

if __name__ == "__main__":
    main()
