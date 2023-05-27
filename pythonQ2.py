# creating a function which takes text as input and returns Yes or No based on the given conditions
def func(text):
    # counting frequency of each letter
    letters = {}
    for i in text:
        if i in letters.keys():
            letters[i] = letters[i] + 1
        else:
            letters[i] = 1
            
    # frequency of frequencies
    
    freq = {}
    for i in letters.values():
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    
    # making a list of unique values of frequency
    
    val = list(set(letters.values()))
    
    # if frequency of eacch element is same then print True (Ex: "aabbcc")
    if len(val) ==1:
        return "Yes"
    
    # If there are two different frequencies then following conditions will be checked
    elif len(val) ==2:
        
        # If one of the letters occurs only once then it can be eleminated to obtain True condition (Ex: "abbbccc")
        if min(val) ==1 and freq[1] == 1:
            return "Yes"
        
        # If frequency of both frequencies is more than one then absolute difference of frequencies must be 1 and frequency of maximum       frequency must be 1 to obtain True condition (Ex: "aaaabbbccc")
        elif abs(val[0] - val[1]) == 1 and freq[max(freq.keys())] ==1:
            return "Yes"
        
        else:
            return "No"
        
    else:
        return "No"

# creating multiple strings for testing
text = ["abc", "abcc", "aaabbbcccd", "aabccc", "abccc", "aaabbbcc"]
# Calling function for each string
for i in text:
    result = func(i)
    print(f"For the string '{i}', returned value is '{result}'")