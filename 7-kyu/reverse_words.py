# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# First solution
# def reverse_words(text):
#     text = text.split(' ')
#     new_list = []
#     for word in text:
#         new_list.append(word[::-1])
#     return " ".join(new_list)

#Refactored solution
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))
