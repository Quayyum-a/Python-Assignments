def  get_anagram(word1:str, word2:str)->bool:
    for count in word1:
        if word1.count(count) != word2.count(count):
            return False
    return True