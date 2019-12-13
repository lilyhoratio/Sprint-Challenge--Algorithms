'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    
    ## if remaining word is less than length of "th"
    if (len(word) < 2):
        return 0
    
    ## if the first two letters are "th", 
    if (word[0:2] == "th"):
        return 1 + count_th(word[1:])
    
    


def count_th_loop(word):

