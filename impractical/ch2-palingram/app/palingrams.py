"""Find all word-pair palingrams in a dictionary file"""
import load_dictionary
import random

word_list = load_dictionary.load('../resources/words.txt')

# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word + " " + rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-1] in words:
                    pali_list.append((rev_word[:end-i] + " " + word))
    return pali_list

def get_random_palingram():
    """"Return a random palingram using find_palingrams()"""
    random_palingram = random.choice(find_palingrams())
    return random_palingram

"""
palingrams = find_palingrams()

#sort palingrms on first word
palingrams_sorted = sorted(palingrams)

# display list of plaingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
    
"""
