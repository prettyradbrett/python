import anagrams

def generate_anagrams(keyword):
    result = anagrams.get_anagrams_of_keyword(keyword.replace("_", " "))
    if len(result) == 0:
        return "no results"
    output = ""
    for r in result:
        output += r + "\n"
    return output 