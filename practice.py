def sum(a,b):
    return a + b
print(sum(2,3))

def even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(even_or_odd(int(5)))


def fizzbuzz(num):
    newlist = []
    for i in range(1,num+1):
        if (i % 3) == 0 and (i % 5)== 0:
            newlist.append("fizzbuzz")
        elif (i % 3) == 0:
            newlist.append("fizz")
        elif(i % 5) == 0 :
            newlist.append("Buzz")
        else:
            newlist.append(str(i))
            
        newstring = " ".join(newlist)
    return newstring
print(fizzbuzz(num=15))

def count_vowels(word):
    words = str(word).lower()
    character = 0
    vowels = "aeiou"
    for i in words:
        for x in vowels:
            if i == x :
                character +=1
    return character
print(count_vowels("Mpho"))

def is_palindrome(phrase):
    j = -1
    phrase = str(phrase)
    for i in phrase:
        if i != phrase[j]:
            return False
        else:
            return True
    return
print(is_palindrome("rorator"))

def sum_even():
    numbers = [1,3,5]
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total += i
    return total
print(sum_even())


