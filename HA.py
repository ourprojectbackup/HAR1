palindromeList =[]
def allPossibleSubstring(data,size):
    lengthOfData = len(data)
    i = 0
    while (i + size <= lengthOfData ):
        substring = data[i:i+size+1]
        i +=1
        checkPalindrome(substring)

def checkPalindrome(data):
    originalString = data
    reverseString = data[::-1]
    if(originalString==reverseString):
        palindromeList.append(originalString)
        print("Found a Palindrome of length "+str(len(data))+": ")
        print(originalString)
        print(reverseString)
    
input = input("Enter the String :")
length = len(input)
while length>0:
    allPossibleSubstring(input,length-1)
    if(len(palindromeList) >0):
        break
    length -=1

if(len(palindromeList) >0):
    print("\n\nThe Longest Palindrome Found is :")
    for str in palindromeList:
        print(str)
else:
    print("No Palindromeic Substring found in the entered String :"+input)





