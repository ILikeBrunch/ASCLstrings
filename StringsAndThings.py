     
'''
Created 10/5/2021
Strings and THings
Documentation
'''
word = ()
total = ()
start = ()
numberChars = ()
direction = ()

def ls(numberChars, word):
    '''
    calls word and variable 'numberChars' from main
    Deletes the 'numberChars' amt of characters starting with the first character (leftmost)
    Inputs 'numberChars' number of # at the end of the string
    start = before first character
    return the string with 'numberChars' amt of characters deleted, starting from the first character (leftmost) AND 'numberChars' amt of # after the last character (rightmost)
    '''
    
    final_string = ()
    final_string = word
    word = word.split()
    sliced = final_string[numberChars:] + "#" * numberChars
    print('ls version: ', sliced)

def rs(numberChars, word):
    '''
    calls word and variable 'numberChars' from main
    Deletes the 'numberChars' amt of characters starting with the last character (rightmost)
    Inputs 'numberChars' number of # at the beggining of the string
    start = after last character
    return the string with 'numberChars' amt of characters deleted, starting from the last character (rightmost) AND 'numberChars' amt of # before the first character (leftmost)
    '''
    final_string = ()
    final_string = word
    word = word.split()
    sliced = "#" * numberChars + final_string[:numberChars] 
    print('rs version:', sliced)
    
def lc(numberChars, word):
    '''
    calls word and variable 'numberChars' from the main
    takes 'numberChars' amt of characters starting with the first character (leftmost) and moves 'numberChars' amt of characters to after the last character (rightmost)
    start = before first character
    return the string with the first 'numberChars' amt of characters moved to after the last (rightmost) character
    '''
    part = word[0:numberChars] 
    print('lc version:' , word[numberChars:] + part)
    
def rc(numberChars, word): 
    '''
    calls word and variable 'numberChars' from the main
    takes 'numberChars' amt of characters starting with the last character (rightmost)and moves 'numberChars' amt of characters to before the first character (leftmost)
    start = after last character
    return the string with the last 'numberChars' amt of characters moved to before the first (leftmost) character
    '''

def mc(start,total,numberChars,direction, word):
    '''
    calls word and variable 'numberChars', 'start', 'total', 'direction' from the main
    start = before position inputted (instead of leftmost and rightmost it is start position)
    start at position 'start' out of 'total' and move 'numberChars' amt of characters in the direction 'direction'
    return the string following the above arguements
    '''
    
    start = start -1                                                                                                    #Fixes user input 
    def rightrotate(subString, numberChars):                                                          #defines right rotate function
        return leftrotate(subString, len(subString) - numberChars)                           #inverts left rotate ot become right rotate
    def leftrotate(subString,numberChars):                                                             #defines left rotate
        segment = subString[numberChars : ] + subString[0 : numberChars]               #rotates section of word
        return segment
        
    if direction == 'L':
        total = total + start                                                                                           
        subString = word[start:total]                                                                           #This creates a segment of the word that the user wants to change
        print(word[:start] + leftrotate(subString,numberChars) + word[total:])           #DEBUG | REMOVE
        return (word[:start] + leftrotate(subString,numberChars) + word[total:])        #Returns the beginning of the word, the rotated segment, and the end
    
    if direction == 'R':
        total = total + start
        subString = word[start:total]                                                                           #This creates a segment of the word that the user wants to change
        print(word[:start] + rightrotate(subString, numberChars) + word[total:])        #DEBUG | REMOVE
        return (word[:start] + rightrotate(subString, numberChars) + word[total:])     #Returns the beginning of the word, the rotated segment, and the end
    
    
def rev(start, total, word):
    '''
    reverse order of word 
    call word from main, start with position 'start' out of 'total' 
    return the string starting with the last character (rightmost) and ending with the first (leftmost)
    '''
    if start <= 0:
        print('Error: Starting position must be greater then 0.') #DEBUG REMOVE WHEN NEEDED
        return 'Error: Starting position must be greater then 0.'
    
        main()
    start = start -1                                                            #Dealing with offset by subtracting 1
    total = total - 1                                                                   #Dealing with offset by subtracting 1
    end = start+total                                                             #This calculates the end point by adding the total amount of chars effected
    wordList = list(word)                                                         #Converts desired word to list
    if start > 0:
        revChar = wordList[end:start-1:-1]
    else:
        revChar = wordList[:end+1]
        revChar = revChar[::-1]
    del wordList[start:end+1]                                                #deletes section from original function
    wordList.insert(start, revChar)                                          #This puts the reversed segment list into the wordList list
    flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
    output = ''.join(flatList)                                                          #This converts the list into a string
    print('Output: ' + output) #DEBUG REMOVE WHEN NEEDED
    return output
    
    
def main():
    '''
    User puts in the word; word=string
    word = user input that is being altered
    User puts in how many characters they want to be altered
    numberChars = amount of characters that will be altered 
    start = starting position
    direction = right or left, what direction are the 'numberChars' amount of characters moved
    '''
    
    word = input('enter word you would like altered')
    numberChars = int(input('how many characters do you want altered?'))
    start = input('where would you like to start altering the string?')
    direction = input('what direction would you like to alter towards, L or R?')    
    
    ls(numberChars, word)
    lc(numberChars, word)
    rs(numberChars, word)
    rc(numberChars, word)
    rev(start, total, word)
    mc(start,total,numberChars,direction, word)

if __name__ == "__main__":
    main()
