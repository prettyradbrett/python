"""Find all anagrams of a given keyword in a dictionary file"""
import load_dictionary
from collections import Counter

word_list = load_dictionary.load('../resources/words.txt')

def get_anagrams_of_keyword(keyword):
    anagram_list = []

    print("Input keyword = {}".format(keyword))
    keyword = keyword.lower().replace(" ","")
    keyword_count = Counter(keyword)

    for word in word_list:
        word = word.lower()
        if word != keyword:
            if Counter(word) == keyword_count:
                anagram_list.append(word)
                print(word)
    return anagram_list