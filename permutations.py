def generate_permutations(input_string):
    if len(input_string) == 1:
        return [input_string]

    permutations = []
    for i in range(len(input_string)):
        char = input_string[i]
        remaining_chars = input_string[:i] + input_string[i+1:]
        for perm in generate_permutations(remaining_chars):
            permutations.append(char + perm)
            print(permutations)

    return permutations

input_str = "cat"  # Replace with your desired input string
permutations_list = generate_permutations(input_str)

print(f"All the strings that can be formed from '{input_str}':")
for word in permutations_list:
    print(word)


# def generate_permutations(input_string):
#     words = []
    
#     # Create a list to hold the initial permutation
#     current_perms = [('', input_string)]
    
#     # Iterate until there are no more permutations to generate
#     while current_perms:
#         prefix, remaining = current_perms.pop()
        
#         # Base case: If there are no more characters remaining, add the prefix as a word
#         if len(remaining) == 0:
#             words.append(prefix)
        
#         # Generate new permutations by appending each remaining character to the prefix
#         for i in range(len(remaining)):
#             char = remaining[i]
#             new_prefix = prefix + char
#             new_remaining = remaining[:i] + remaining[i+1:]
#             current_perms.append((new_prefix, new_remaining))
    
#     return words

# input_str = "hello"  # Replace with your desired input string
# permutations_list = generate_permutations(input_str)

# print(f"All the strings that can be formed from '{input_str}':")
# for word in permutations_list:
#     print(word)

