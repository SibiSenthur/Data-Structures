class Solution:
    def decodeString(self, s: str) -> str:
         # instantiate stacks to store the number and the string to repeat.
        repeatStr = []
        numRepeat = []
        
        # initialize empty strings. One to store a multidigit number and other one to store the decoded string. 
        tempNum = ''
        decodedStr = ''        
        
        # start iterating throught the encoded string
        for char in s:
            # check if the char is a digit. 
            if char.isdigit():
                tempNum += char # add the number to tempNum
                
            # check if the char is an opening bracket
            elif char == '[':
                repeatStr.append(decodedStr)
                numRepeat.append(tempNum)
                tempNum = ''
                decodedStr = ''
                
            # check when the bracket closes
            elif char == ']':
                decodedStr = repeatStr.pop() + (decodedStr * int(numRepeat.pop()))
                
            # else build the substring to repeat
            else:
                decodedStr += char            
                
        return decodedStr
        