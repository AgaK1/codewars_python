#Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.



def get_count(input_str):
    result = 0   
    for vowel in input_str:
        if(vowel == "a" or vowel == "e" or vowel == "i"or vowel == "u" or vowel == "o"):
            result+=1
    return result