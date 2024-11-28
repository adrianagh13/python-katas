def construct_word(words):
    result = ""

    for i, word in enumerate(words):
        if i < len(word):
            result += word[i]
        else:
            print(f"The word {word} is not long enough to get the corresponding index letter")
    
    return f"The resulting word is {result}"
