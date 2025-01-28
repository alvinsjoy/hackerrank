"""
You are given a string word. For each alphabetical character in word, replace it with a vowel following a cyclic pattern of ['a', 'e', 'i', 'o', 'u']. Preserve the original case. Non-alphabetical characters remain unchanged. Return the resulting string.

Example 1
Input: "Hello"
Output: "Iilla"
"""
def replace_letters(word):
    replacement_pattern = ['a', 'e', 'i', 'o', 'u']

    result = ""

    for char in word:
        if char.isalpha():
            position = ord(char.lower()) - ord('a')
            replacement = replacement_pattern[position % 5]
            if char.isupper():
                replacement = replacement.upper()
            result += replacement
        else:
            result += char

    return result


word = input("Enter a word: ")
transformed_word = replace_letters(word)
print(f"Transformed word: {transformed_word}")
