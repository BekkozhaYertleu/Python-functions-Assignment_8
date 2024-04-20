#Ex 1
def count_unique_elements(my_list: list) -> int:
    unique_set = set()

    for num in my_list:
        unique_set.add(num)

    return len(unique_set)

# print (count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]))

#Remove duplicates
def remove_duplicates(my_list: list) -> list:
    seen = set()
    unique_list = []

    for num in my_list:
        if num not in seen:
            seen.add(num)
            unique_list.append(num)

    return unique_list
# print(remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]))

# Exercise-3: Reverse a list
def reverse_list(my_list: list) -> list:
    reversed_list = my_list[::-1]
    return reversed_list

# print(reverse_list([1, 2, 3, 4, 5]))

# Exercise-4: Find the maximum value in a list

def max_value(my_list: list) -> int:
    maximum_value = max(my_list)
    return maximum_value

# print(max_value([1, 2, 3, 4, 5])) 

# Exercise-5: Find the minimum value in a list

def min_value(my_list: list) -> int:
    minimum_value = min(my_list)
    return minimum_value

# print(min_value([1, 1, 1, 1, 2, 2, 2, 5, 3, 3,]))

# Exercise-6: Sum all values in a list
def sum_values(my_list: list) -> int:
    total_sum = 0
    for num in my_list:
        total_sum += sum
    return total_sum

# print(sum_values([1, 1, 3, 4, 6, 7, 8, 8, 876]))

# Exercise-7: Find the average of a list
def average(my_list: list) -> float:
    list_sum = sum(my_list)
    list_length = len(my_list)
    if list_length == 0:
        return 0
    return list_sum / list_length
print(average([3, 44, 22, 11, 33, 54, 232]))

# Exercise-8: Find the index of an element in a list

def find_index(my_list: list, element: int) -> int:
    for i, num in enumerate(my_list):
        if num == element:
            return i
    return -1

print(find_index([1, 2, 3, 4, 5], 3))  # Output should be 2
print(find_index([1, 2, 3, 4, 5], 6))  # Output should be -1

# Exercise-9: Check if a list is sorted

def is_sorted(my_list: list) -> bool:
    for i in range(len(my_list)  -1 ):
        if my_list[i] > my_list[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5]))  # Output should be True
print(is_sorted([1, 3, 2, 4, 5])) 


# Exercise-10: Count the frequency of an element in a list
def count_frequency(my_list: list, element: int) -> int:
    frequency = 0
    for num in my_list:
        if num == element:
            frequency += 1
    return frequency

print(count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3)) 

# Exercise-11: Find the mode of a list
from collections import Counter

def find_mode(my_list: int) -> int:
    counts = Counter(my_list)
    mode = max(counts, key = counts.get)
    return mode

print(find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]))  # Output: 2

# Exercise-12: Remove all occurrences of an element in a list
def remove_all(my_list: list, element: int) -> list:
    new_list = [x for x in my_list if x != element]

    return new_list
print(remove_all([1, 3, 4, 5, 6, 34534, 55, 5,5,5,5,5,5,5,5,5], 3))


# Exercise-13: Rotate a list to the left by k positions
def rotate_left(my_list: list, k: int) -> int:
    k = k % len(my_list)
    rotated_left = my_list[k:] + my_list[:k]

    return rotated_left

print(rotate_left([1, 2, 3, 4, 5, 6], 6))
# calculate the effective rotation index by taking the modulus %


# Exercise-14: Rotate a list to the right by k positions
def rotate_right(my_list: list, k: int) -> list:
    # Calculate the effective rotation index
    k = k % len(my_list)
    
    # Rotate the list using slicing
    rotated_list = my_list[-k:] + my_list[:-k]
    
    return rotated_list

# Test the function with example inputs
print(rotate_right([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

# Exercise-15: Find the intersection of two lists

def find_intersection(list1: list, list2: list) -> list:
    # Convert both lists to sets and find their intersection
    intersection_set = set(list1) & set(list2)

    # Convert the intersection set back to a list
    intersection_list = list(intersection_set)

    # Return the intersection list
    return intersection_list

print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6])) 

# Exercise-16: Find the union of two lists

def find_union(list1: list, list2: list) -> list:
# Convert both lists to sets and find their union
    union_set = set(list1) | set(list2)
# Convert the union set back to a list
    union_list = list(union_set)
    return union_list

# Test the function with example inputs
print(find_union([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]

# Exercise-17: Find the difference of two lists
def  find_difference(list1: list, list2: list) -> list:
    difference = []

    for element in list1:

        if element not in list1:
            if element not in list2:

                difference.append(element)
    return difference

print(find_difference([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [1, 2]
# efficient solution
def find_difference(list1: list, list2: list) -> list:
    # Convert the lists to sets for efficient membership testing
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the elements that are present in set1 but not in set2
    difference = list(set1 - set2)
    
    # Return the difference list
    return difference

# Test the function with example inputs
print(find_difference([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [1, 2]

#  Exercise-1 (Longest Consecutive Sequence): Diamand
def longest_consecutive(my_list: list[int]) -> int:
    num_set = set(my_list)

    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            currents_num = num
            current_length = 1

            while currents_num + 1 in num_set:
                currents_num += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4

# Exercise-2 (Find missing number): Diamond
def find_missing(my_list: list[int]) -> int:
    n = len(my_list) + 1  # n is the size of the list plus 1 (since one number is missing)
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given list
    actual_sum = sum(my_list)
    
    # The difference between the expected sum and the actual sum is the missing number
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Test the function with example input
print(find_missing([1, 2, 4]))  # Output: 3

# Exercise-3 (Find duplicate number):
def find_duplicate(my_list: list[int]) -> int:
    # Initialize the slow and fast pointers
    slow = my_list[0]
    fast = my_list[0]
    
    # Move the pointers in the sequence until they meet
    while True:
        slow = my_list[slow]
        fast = my_list[my_list[fast]]
        if slow == fast:
            break
    
    # Reset one pointer to the start of the sequence
    slow = my_list[0]
    
    # Move both pointers at the same speed until they meet
    while slow != fast:
        slow = my_list[slow]
        fast = my_list[fast]
    
    # The meeting point is the duplicate number
    return slow

# Test the function with example input
print(find_duplicate([1, 3, 4, 2, 2]))  # Output: 2


# Exercise-4 (Group Anagrams):
# Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
# takes a list of strings (all lowercase letters), groups the anagrams together, 
# and returns a list of lists of grouped anagrams.
from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    # Initialize a defaultdict to store groups of anagrams
    anagram_groups = defaultdict(list)
    
    # Iterate over each word in the input list
    for word in words:
        # Sort the letters of the word to create a canonical form
        sorted_word = ''.join(sorted(word))
        
        # Append the word to the list of its anagrams in the dictionary
        anagram_groups[sorted_word].append(word)
    
    # Return the values of the dictionary (lists of anagrams)
    return list(anagram_groups.values())

# Test the function with example input
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Exercise-5: collatz_sequence_length

def collatz_sequence_length(n: int, memo={1: 0}) -> int:
    if n not in memo:
        if n % 2 == 0:
            memo[n] = 1 + collatz_sequence_length(n // 2, memo)
        else:
            memo[n] = 1 + collatz_sequence_length(3 * n + 1, memo)
    return memo[n]

# Test the function with example input
print(collatz_sequence_length(6))  # Output: 8
print(collatz_sequence_length(27))  # Output: 111



