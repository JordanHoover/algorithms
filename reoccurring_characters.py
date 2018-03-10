# find the first reoccurring character in a String


# hard code a test string
char_string="ASDFJNVEIWOSLKJF"


def find_reoccurring_char(char_string):
    # create an empty dict object
    counts = {}

    for char in char_string:
        if char in counts:
            return char
        else:
            counts[char]=1
    # if reoccurring char was not found        
    return "no recurring characters"

print(find_reoccurring_char(char_string))

