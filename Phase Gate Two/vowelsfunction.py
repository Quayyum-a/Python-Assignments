def get_vowels(word:str)->int:
    counter = 0
    for count in word:
        if count in 'a,e,i,o,u':
            counter += 1
    return counter