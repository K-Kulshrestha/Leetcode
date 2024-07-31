def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return the indices as 1-based
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    # Since there is exactly one solution, we should never reach here
    return []

def main():
    # Example Usage:
    numbers = [2, 7, 11, 15]
    target = 9
    result = twoSum(numbers, target)
    print(f"The indices of the two numbers that add up to {target} are: {result}")

if __name__ == "__main__":
    main()
