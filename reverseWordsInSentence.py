#reverse the words in a sentence
def reverseWord(str):
    word = ""
    for i in range(len(str)):
        word += str[(len(str)-1)-i]
    return word


def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    strs = our_string.split(" ")
    new_strs = ""
    for i in strs:
        new_strs += reverseWord(i) + " "

    return new_strs[:-1]

# Test Cases

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail", word_flipper('water'))
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail", word_flipper('This is an example'))
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail", word_flipper('This is one small step for ...'))
