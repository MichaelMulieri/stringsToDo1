"""Remove Blanks
Create a function that, given a string, returns all of that strings contents, but without blanks. 
If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic"."""

def closeGap(str):
    str = str.split(' ')
    print(str)
    for i in range(len(str)):
        if str[i] == ' ':
            for j in range(i,len(str)-1):
                temp = str[j]
                str[j] = str[j+1]
                str[j+1] = temp
            str[:-1]
    newString = ''
    for char in str:
        newString += char
    print(newString)
    return newString


closeGap(" Pl ayTha tF u nkyM usi c ")


"""Get Digits
Create a JavaScript function that given a string, returns the integer made from the strings digits. 
Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680."""

def getDigits(str):
    digits=['0','1','2','3','4','5','6','7','8','9']
    str_arr=list(str)
    print(str_arr)

    i=0
    while(i < len(str_arr)-1):
        if str_arr[i] not in digits:
            for j in range(i,len(str_arr)-1):
                temp=str_arr[j]
                str_arr[j]=str_arr[j+1]
                str_arr[j+1]=temp
            print(str_arr.pop())
        i+=1

    return_str=''
    for char in str_arr:
        return_str+=char
    print(return_str)
    return return_str

getDigits("0s1a3y5w7h9a2t4?6!8?0")

"""Acronyms
Create a function that, given a string, returns the strings acronym (first letters only, capitalized). 

Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 

Given "Live from New York, it's Saturday Night!", return "LFNYISN".
"""
def acronym(str):
    acroString = ''
    sepList = str.split(' ')
    for i in range(len(sepList)-1):
        if len(sepList[i]) > 0:
            oneWord = list(sepList[i])
            acroString += oneWord[0].capitalize()
    print(acroString)
    return acroString


acronym(" there's no free lunch - gotta pay yer way. ")
acronym("Live from New York, it's Saturday Night!")

"""Zip Arrays into Dictionary
Dictionaries are sometimes called maps because a key (string) maps to a value. 
Given two arrays, create an associative array (map) containing keys of the first, 
and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}."""

def zip(arr1, arr2):
    dictZip = {}
    for i in range(len(arr1)):
        dictZip[arr1[i]] = arr2[i]
    print(dictZip)
    return dictZip

zip(["abc", 3, "yo"], [42, "wassup", True])


"""Invert Hash
Dictionaries are also called hashes (well learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys. 

Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}."""

def invertHash(assocArr):
    newKey = list(assocArr.values())
    newVal = list(assocArr)
    newDict = {}
    for i in range(len(newKey)):
        newDict[newKey[i]] = newVal[i]
    print(newDict)
    return newDict

"""def invertHash(dict):
    new_dict={}
    for key,value in dict.items():
        new_dict[value]=key
    print(new_dict)
    return new_dict"""

invertHash({"name": "Zaphod", "charm": "high", "morals": "dicey"})
    

    




