# Download required module before running the file
'''
pip install nltk==3.5
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
'''
# importing required libraries
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# creating a function which takes a paragraph as a input and returns the count of parts of speech
def pos(para):
    # Converting paragraph into individual words
    text = word_tokenize(para)
    
    # tagging each word with part of speech tags
    data = pos_tag(text)
    
    # tags for verbs, nouns, pronouns, and adjectives
    noun_tags = ["NN", "NNP", "NNPS", "NNS"]
    pronoun_tags = ["PRP", "PRP$", "WP", "WP$"]
    verb_tags = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
    adjective_tags = ["JJ", "JJR", "JJS"]
    
    # counting tags for each part of speech
    dic = { "nouns": 0, "pronouns": 0, "verbs": 0, "adjectives": 0}
    for i in range(len(data)):
        if data[i][1] in noun_tags:
            dic["nouns"] = dic["nouns"] + 1
        if data[i][1] in pronoun_tags:
            dic["pronouns"] = dic["pronouns"] + 1
        if data[i][1] in verb_tags:
            dic["verbs"] = dic["verbs"] + 1
        if data[i][1] in adjective_tags:
            dic["adjectives"] = dic["adjectives"] + 1
    return dic
        
# Initilizing paragraphs
para1 = "The Chinese love dragons. They believe that the dragon is powerful and wise and brings good luck. There are many temples built to honor the dragons in China. Chinese dragons are snake-like, wingless animals with four legs and five claws on each leg. According to stories, Chinese dragons have a magic pearl which gives them the power to fly and go into heaven. The Chinese believe that dragons control water, rainfall, hurricane, and floods."

para2 = "Korean dragons are the most kind-hearted of all the dragons. A Korean dragon is a snake-like, wingless animal with a long beard. A Korean dragon has four legs with four claws on each leg. In Korean stories, dragons are water animals, which control water and farming."

para3 = "Japanese dragons are large, wingless, snake-like animals with three claws on each foot. Japanese believe that dragons are water animals that control rainfall and water. According to Japanese stories, dragons were first born in Japan. Dragons are very popular in Japan and are used a lot in art, music and architecture."

# Calling the function to print the paragraph and count the parts of speech
paras = [para1, para2, para3]
for i in paras:
    print("Counting parts of speech in the below paragraph\n")
    print(i)
    result = pos(i)
    print(f"The count of each part of speech is as follows:\n{result}")