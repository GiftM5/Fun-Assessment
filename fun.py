def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    #enter your code here
    dogs_years = 0
    human_years = int(input("Input dog's age in human years: "))
    while human_years > 20 :
        human_years = int(input("Input dog's age in human years that is not more than 20 years "))
    for i in range(1, human_years+1):
        if i ==1 or i == 2:
            dogs_years = dogs_years + 10.5
        else:
            dogs_years = dogs_years + 4


    print(f"The dog's age in dog's years is {int(dogs_years)}")
dog_years()


def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """
    #enter your code here
    new_list = []
    for i in range(1,num+1): 
        if (i % 3) == 0 and (i % 5) == 0:
            new_list.append("FizzBuzz")
        elif (i % 3) == 0:
            new_list.append("Fizz")
        elif (i % 5) == 0:
            new_list.append("Buzz")
        else:
            new_list.append(str(i))
       
        new_string = " ".join(new_list)
    return new_string 
print(fizzbuzz(num=15))
    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    # enter your code here
    if type(sentence) != str :
        raise ValueError("You have entered a number instead of a sentence.")
    
    sentence = str(sentence)
    names = sentence.split()
    
    dictionary = {}
    for word in names:
        dictionary[word]= len(word)
    return dictionary
   
print(word_lengths("Aunty Yankho is amazing"))      
   

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
   #enter your code here
    if number < 0 :
            raise ValueError("You entered a negative number") 
    total = 0
    for i in str(number):
        if i.isdigit():
            total += int(i)**(3)
        else:
            return None    
       
    return total                 
   
print(cube_sum(123))
    