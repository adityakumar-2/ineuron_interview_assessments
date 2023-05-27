# importing re module to split the input string using multiple delimiters
import re

# defining a function to return the lenth of word with maximum frequency in a sentence
def len_of_max_freq_word(sent):
    # Taking string input
    text = sent
    
    # converting string into a list considering multiple delimiters for the string
    word_list = re.split(" |,|;|:",text)
    
    # initilizing a dictionary for unique words and their frequency in the list
    frequency = {}
    
    # adding the words in string as keys and their frequency as values in the dictionary
    for word in set(word_list):
        frequency[word] = word_list.count(word)
    
    # finding the maximum frequency
    max_freq = max(frequency.values())
    
    # making a list of lenghts of maximum frequency words
    lenghts = []
    for key, value in frequency.items():
        if value == max_freq:
            hf_word = lenghts.append(len(key))
    
    # returning the lenght of longest word with maximum frequency
    return max(lenghts)

# Initilizing input strings
str1 = "write write write all the number from from from 1 to 100"
str2 = "write all the number from 1 to 100" # if multiple words with same max frequency is present then max lenth is returned
str3 = "write write write all the number from from from 1 1 1 1 to 100"

# list of strings
strs = [str1, str2, str3]

for i in strs:
    print("For the below sentence:")
    print(i)
    print("\n")
    result = len_of_max_freq_word(i)
    print(f"The length of word with maximum frequency is {result}\n")