
import random
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

def replacechar(str1):
    char = str1[0]
    str1 = str1.replace(char,'$')
    str1 = char + str1[1:]
    return str1
    
def add_addition(str1):
    if len(str1) > 2:
        if str1[-3:]== "ing":
            str1=str1+"ly"
        else:
            str1=str1+"ing"
    return str1

def find_longest_word(words):
    
    words_list=words.split(' ')
    word_len = []
    
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
   
        
def sort_words(words):
    words_list = words.split(',')
    print(','.join(sorted(list(set(words)))))
    
def addchars(str1):
    strlen=len(str1)
    str2=str1[-2:]
    for i in range(0,4):
        str1+=str2
    return str1

        
def caesar_encrypt(realText, step):
    outText = []
    cryptText = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in realText:
        if eachLetter in uppercase:
                index = uppercase.index(eachLetter)
                crypting = (index + step) % 26
                cryptText.append(crypting)
                newLetter = uppercase[crypting]
                outText.append(newLetter)
        elif eachLetter in lowercase:
                index = lowercase.index(eachLetter)
                crypting = (index + step) % 26
                cryptText.append(crypting)
                newLetter = lowercase[crypting]
                outText.append(newLetter)
    return outText

def check_numbers(numbers):
    numberslist = []
    numberslist = numbers.split(' ')
    for i in range(0,len(numberslist)):
        if numberslist[i]==numberslist[i+1]:
            return True
        else:
            return False
        
        
def find_average(numberslist):
    total=0
    for i in range(0,len(numberslist)):
        total = total+numberslist[i]
    
    average=total/len(numberslist)
    return average
    
def is_prime(number):
    if int(number) > 1:
        for i in range(2,(int(number)//2)+1):
            if number == 0:
                print("number is NOT prime!")
                break
            else:
                print("number is PRIME!")
                
def findthe3rd(numberlist):
    for i in range(0, len(numberlist)):
        for j in range(0, len(numberlist)-1):
            if numberlist[j]>numberlist[j+1]:
                swap=numberlist[j]
                numberlist[j]=numberlist[j+1]
                numberlist[j+1]=swap
    return numberlist[2]
    
    
print(findthe3rd([4,6,2,7,8,6,4,6]))
#primenumber=input("Enter number:")
#is_prime(primenumber)
      
# numbers=input("Enter numbers:")
# print(check_numbers(numbers))

# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))

# setstring = input("Please enter mized numbers with comma seperated:")
# setlist = set(setstring)
# print(setlist)



# code = caesar_encrypt('En Buyuk Fenerbahce', 4)
# print(code)


# mystring=input("Enter string:")

# print(char_frequency(mystring))
# print(replacechar(mystring))
# print(add_addition(mystring))
# print(find_longest_word(mystring))      
# sort_words(mystring)
# print(addchars(mystring))

