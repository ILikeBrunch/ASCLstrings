def main():
    start=3

    total=3
    numberChars=2
    direction="R"
    word= "COMPUTER"
    #mc(start,total,numberChars,direction, word)
    rev(start,total,word)
    #mc(start,total,numberChars,direction,word)
    
    
def mc(start,total,numberChars,direction, word):
    start = start -1
    def rightrotate(subString, numberChars):
        return leftrotate(subString, len(subString) - numberChars)
    def leftrotate(subString,numberChars):
        tmp = subString[numberChars : ] + subString[0 : numberChars]
        return tmp
        
    if direction == "L":
        total = total + start
        subString = word[start:total]
        print(word[:start] + leftrotate(subString,numberChars) + word[total:])
        return (word[:start] + leftrotate(subString,numberChars) + word[total:])
    
    if direction == "R":
        total = total + start
        subString = word[start:total]
        print(word[:start] + rightrotate(subString, numberChars) + word[total:])
        return (word[:start] + rightrotate(subString, numberChars) + word[total:])
 
    
    
def rev(start, total,word): 
    if start <= 0:
        return "Error: Starting position must be greater then 0."
        main()
    start = start -1                                                            #Dealing with offset by subtracting 1
    total = total - 1                                                                   #Dealing with offset by subtracting 1
    end = start+total                                                             #This calculates the end point by adding the total amount of chars effected
    wordList = list(word)                                                         #Converts desired word to list
    if end > len(word):
        print("Error: Desired segment of string not reachable (Word too short)")
        return "Error: Desired segment of string not reachable (Word too short)"
    if start > 0:
        revChar = wordList[end:start-1:-1]
    else:
        revChar = wordList[:end+1]
        revChar = revChar[::-1]
    del wordList[start:end+1]                                                #deletes section from original function
    wordList.insert(start, revChar)                                          #This puts the reversed segment list into the wordList list
    flatList = [item for sublist in wordList for item in sublist]        #This flattens the list inside the list into one list            
    output = ''.join(flatList)                                                          #This converts the list into a string
    print("Output: " + output)
    return output
    
    
    
if __name__ == '__main__':
    main()
