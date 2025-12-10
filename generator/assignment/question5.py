# Q5: Write a generator that yields only words starting with a vowel from a given sentence
# Example:
# Input → "Apples are awesome and bananas are boring"
# Output → ['Apples', 'are', 'awesome', 'and', 'are']

def words_starting_with_vowel(sentence):
    vowels = 'aeiouAEIOU'
    for word in sentence.split():
        if word[0] in vowels:
            yield word 

# Example usage:
sentence = "Apples are awesome and bananas are boring"
result = list(words_starting_with_vowel(sentence))
print(result)








