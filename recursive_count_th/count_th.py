'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    """ 
    Example call with "brother" word:

    brother - br - 0
        rother - ro - 0
            other - ot - 0
                ther - th - 1
                    her - he - 0
                        er - er - 0
    """

    ## if remaining word is less than length of "th"
    if (len(word) < 2):
        return 0
    
    ## if the first two letters are "th"
    if (word[0:2] == "th"):
        return 1 + count_th(word[1:])

    ## if there is no match, call function recursively but don't increment count
    return count_th(word[1:])

def count_th_loop(word):
    count = 0
    for i in range(len(word)):
        if word[i:i+2] == "th":
            count+=1
    return count


print(count_th_loop("brother"))

