# def isAnagram(s: str, t: str) -> bool:
#     return sorted(s) == sorted(t)


# need to review this method more efficient and takes O(n) time compared to O(nlogn)
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Create a frequency count for each character in s
    count_s = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    # Create a frequency count for each character in t
    count_t = {}
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    # Compare the two frequency counts
    return count_s == count_t

# Example usage
def main():
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("hello", "bello", False),
        ("aabbcc", "abcabc", True)
    ]

    for s, t, expected in test_cases:
        result = isAnagram(s, t)
        print(f"isAnagram({s}, {t}) = {result} (expected: {expected})")

if __name__ == "__main__":
    main()
