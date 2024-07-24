def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s):
    res, i = [], 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return res

# Example usage
def main():
    original_strings = ["hello", "world", "this", "is", "a", "test"]
    encoded_string = encode(original_strings)
    print(f"Encoded: {encoded_string}")
    decoded_strings = decode(encoded_string)
    print(f"Decoded: {decoded_strings}")
    
if __name__ == "__main__":
    main()
